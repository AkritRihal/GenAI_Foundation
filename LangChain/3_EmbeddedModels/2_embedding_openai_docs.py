# generating embedding of entire documents and not a particular queries
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model = 'text_embedding_3_large', dimensions=32)

documents = [
    "This is a sample document." 
    "New Delhi is the capital of India and a part of the National Capital Territory of Delhi."
    "New Delhi is the seat of all three branches of the Government of India, hosting the Rashtrapati Bhavan, Sansad Bhavan, and the Supreme Court"
    "It is used for testing purposes.",
]

result = embedding.embed_documents(documents) 

print (str(result))