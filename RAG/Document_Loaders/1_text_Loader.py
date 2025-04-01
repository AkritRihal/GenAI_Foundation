# Reads plain text files and returns it in LangChain documents format

from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
prompt = PromptTemplate(
    template = "Generate a summary of the text {text}",
    input_variables= ['text']
)
parser = StrOutputParser()

# loading docs
loader = TextLoader("summer.txt")
docs = loader.load()
print(type(docs), "\n\n", docs[0])

chain = prompt | model | parser
res = chain.invoke({"text": docs[0].page_content})
print(res)
