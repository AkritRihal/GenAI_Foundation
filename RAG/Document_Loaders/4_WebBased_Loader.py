# used to load and extract text content from web pages
# uses BeautifulSoup for parsing HTML content
# used for static pages mostly
# for dynamic pages use SeleniumURLLoader

from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/acer-swift-go-14-snapdragon-x-plus-16-gb-512-gb-ssd-windows-11-home-sfg14-01-x9c8-thin-light-laptop/p/itmd59652b059190"
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))