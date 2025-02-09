import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape a LinkedIn profile for information,
    Manually scrape a LinkedIn profile for information"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/avelops/1e194f86689869907a669775bf162429/raw/9e2d331f21c22fa2ea9526838598db64ccaa6713/avi_elmaliah-scrapin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
        data = response.json()
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ.get("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)
        data = response.json().get("person")
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/avielmaliah", mock=True
        )
    )
