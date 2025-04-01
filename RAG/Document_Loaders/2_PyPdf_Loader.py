# reads pdf files and returns it in LangChain documents format
# works on page by page method ,  a doc obj for each page

from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("")

docs = loader.load()
print(type(docs), "\n\n", docs)