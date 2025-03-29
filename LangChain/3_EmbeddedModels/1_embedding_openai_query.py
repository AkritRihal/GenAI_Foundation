from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model = 'text_embedding_3_large', dimensions=32)

result = embedding.embed_query('Delhi is the capital of India') 

print (str(result))