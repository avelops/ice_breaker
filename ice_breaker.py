from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

information = """
Morrison was born on December 8, 1943, in Melbourne, Florida, to Clara Virginia (née Clarke; 1919–2005) and Lt.(j.g.) George Stephen Morrison (1919–2008), a future rear admiral in the United States Navy.[15] His ancestors were Scottish, Irish, and English.[16][17][18] In August 1964, Admiral Morrison was commanding U.S. naval forces during the Gulf of Tonkin incident. The following year, in 1965, the incident was a leading pretext used to justify U.S. engagement in the Vietnam War.[19] Morrison had a younger sister, Anne Robin, who was born in Albuquerque, New Mexico in 1947, and a younger brother, Andrew Lee Morrison, who was born in Los Altos, California in 1948.[20]
"""

if __name__ == "__main__":
    load_dotenv()

    summary_template = """
        given the information {information} about a person I want you to create:
        1. a short summary
        2. two facts about them
    """
    # summary_template = """
    #     given the information {information} about an album I want you to create:
    #     1. a short post for social media group recommending the album
    #     2. json form of the details like artist, album name, year issued etc.
    # """

    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatAnthropic(temperature=1, model_name="claude-3-5-sonnet-20241022")
    # llm = ChatOllama(temperature=0,model="phi3.5")
    # llm = HuggingFaceEndpoint(
    #     # repo_id="microsoft/phi-4",
    #     repo_id="deepseek-ai/DeepSeek-R1",
    #     task="text-generation",
    #     max_new_tokens=1000,
    #     do_sample=False,
    #     huggingfacehub_api_token=os.environ.get('HUGGINGFACEHUB_API_TOKEN'),
    # )

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
