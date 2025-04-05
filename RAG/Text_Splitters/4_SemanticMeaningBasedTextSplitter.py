# Semantic Meaning Based Text Splitter is used to split text based on its semantic meaning.
# # This is useful when you want to maintain the context and meaning of the text while breaking it into smaller chunks.

# example the text is about two different topics 

text = """

Spring is one of the most beautiful and eagerly awaited seasons of the year. It marks the transition from the cold, harsh winter to the warm, vibrant summer. Typically occurring between March and June in the Northern Hemisphere, and between September and December in the Southern Hemisphere, spring is a time of renewal, rebirth, and rejuvenation.

The water cycle or hydrological cycle, is a continuous process that moves water through the Earth's atmosphere, surface, and underground. This cycle plays a crucial role in maintaining life, regulating climate, and replenishing water sources. It consists of several key stages: evaporation, condensation, precipitation, and collection.

Terrorism is the unlawful use of violence, intimidation, or threats to achieve political, religious, or ideological objectives. It targets civilians, governments, or institutions, aiming to create fear and instability. Over the years, terrorism has evolved, becoming a major global issue affecting countries, economies, and innocent lives.
"""

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type = 'standard_deviation',
    breakpoint_threshold_amount = 1
)



