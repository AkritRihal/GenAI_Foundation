# separaters are pre defined eg: recursiveTextSplitter
# Text structure based splitters are used to split text based on its structure, such as paragraphs, sentences, or other logical divisions.
# These splitters are designed to maintain the integrity of the text while breaking it into manageable chunks. 

from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
Spring is one of the most beautiful and eagerly awaited seasons of the year. It marks the transition from the cold, harsh winter to the warm, vibrant summer. Typically occurring between March and June in the Northern Hemisphere, and between September and December in the Southern Hemisphere, spring is a time of renewal, rebirth, and rejuvenation.

One of the most striking aspects of spring is the transformation in nature. As temperatures begin to rise, trees that had shed their leaves during winter start to bloom again, covering landscapes in fresh shades of green. Flowers of all kinds—tulips, daffodils, cherry blossoms, and daisies—begin to flourish, filling the air with sweet fragrances and vibrant colors. Birds return from their winter migrations, filling the mornings with cheerful melodies. This rebirth of nature symbolizes hope and new beginnings, making spring a favorite season for many.

Spring also plays a significant role in agriculture. Farmers prepare their fields for planting, taking advantage of the season’s favorable weather conditions. The increased sunlight and rainfall create the perfect environment for crops to grow, ensuring a bountiful harvest later in the year. Many animals also take advantage of the abundance of food, giving birth to their young during this time, ensuring their offspring have the best chance of survival.

Beyond its natural beauty, spring is also a season of celebration. Many cultures and religions hold important festivals during this time, often symbolizing renewal and joy. In India, the festival of Holi is celebrated with bright colors and joyful gatherings, marking the arrival of spring. Easter, celebrated by Christians worldwide, symbolizes resurrection and new life. In Japan, the arrival of cherry blossoms is celebrated with Hanami, a tradition where people gather under the blooming trees to appreciate their fleeting beauty.

Spring’s pleasant weather also encourages outdoor activities. People enjoy picnics, hiking, cycling, and other recreational activities as the days grow longer and sunnier. Parks and gardens become popular spots for relaxation, and the fresh air brings a sense of happiness and well-being. For many, spring represents an opportunity to shake off the gloom of winter and embrace a more active and energetic lifestyle.

Another notable aspect of spring is its impact on human emotions. The increased exposure to sunlight boosts serotonin levels, which helps improve mood and reduce stress. Many people experience a surge in energy and motivation, leading to what is often referred to as "spring fever"—a desire to clean, organize, and start fresh. This is why the tradition of spring cleaning is popular in many cultures, as people take the opportunity to refresh their homes and lives.

In conclusion, spring is a season of change, growth, and beauty. It brings warmth, color, and a sense of renewal, making it one of the most cherished times of the year. Whether through blooming flowers, joyful festivals, or increased energy, spring has a unique way of lifting spirits and inspiring new beginnings.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
)

result = splitter.split_text(text)

print(len(result))
