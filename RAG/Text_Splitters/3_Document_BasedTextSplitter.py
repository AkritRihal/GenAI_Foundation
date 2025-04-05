# Document Based Text Splitter is used to split text based on the document structure. 
# This is useful when dealing with large documents or collections of documents, where you want to maintain the context and relationships between different sections of text.
# ex: a piece of code or text in entirely different language or format


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

text = """
class SpringSeason:
    def __init__(self, temperature, flowers):
        self.temperature = temperature
        self.flowers = flowers

    def describe_season(self):
        print(f"Spring has arrived! The temperature is around {self.temperature}°C.")
        print("The trees are turning green, and flowers are starting to bloom!\n")

    def bloom_flowers(self):
        print("Watch the flowers bloom:")
        for flower in self.flowers:
            print(f"🌸 {flower} is blooming...")
            time.sleep(1)
        print("\nSpring is in full bloom! 🌻🌷🌼")

# Creating an object of SpringSeason
spring = SpringSeason(temperature=20, flowers=["Tulip", "Daffodil", "Cherry Blossom", "Sunflower"])

# Using the class methods
spring.describe_season()
spring.bloom_flowers()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language= 'python',
    chunk_size = 100,
    chunk_overlap = 0,
)

result = splitter.split_text(text)

print(len(result))
