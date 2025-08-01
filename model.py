# from langchain import ChatOpenAI 
from langchain_aws import ChatBedrock
# from langchain_openai import OpenAIEmbeddings

# llm_model = ChatOpenAI(temperature=0)
llm_model = ChatBedrock(
    model_id = "us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name = "us_west-2", 
    temperature = 0
    )

embed_model = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004"
)