from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = "gpt-4")
result = model.invoke("What is the capital of India?")

print(result)  # prints response as well as a lot of metadata
# to only see the reponse 
print(result.content) 