from dotenv import load_dotenv
# from langchain import ChatOpenAI 
# from langchain_aws import ChatBedrock
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# from langchain_openai import OpenAIEmbeddings

load_dotenv()

# llm_model = ChatOpenAI(temperature=0)
# llm_model = ChatBedrock(
#     model_id = "us.anthropic.claude-sonnet-4-20250514-v1:0",
#     region_name = "us_west-2", 
#     temperature = 0
#     )

#  chat model 
llm_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", 
    temperature=0,
)

# embedding model 
embed_model = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004"
)