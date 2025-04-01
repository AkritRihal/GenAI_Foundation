# lets you load multiple files from a directory and returns them in LangChain documents format

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader


loader = DirectoryLoader(
    path = "", # e.g. "docs/"
    glob = " ",  # e.g. "*.pdf" or "*.txt"
    loader_cls = PyPDFLoader, # or TextLoader
)

docs = loader.load()
print(type(docs), "\n\n", docs[0])