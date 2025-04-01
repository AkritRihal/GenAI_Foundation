# used to load CSV files and convert them into LangChain documents - one per row  - by default

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path = "csv filename")

docs = loader.load()

print(len(docs), "\n\n", docs[0])