# allows us to convert the python functions as Runnable
# thus it canbe connected to other runnables

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Generate a joke on {topic}",
    input_variables= ['topic']
)

def word_counter(text):
    return len(text.split())

joke_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        "words": RunnableLambda(word_counter)
        # instead of RunnableLambda(word_counter) we can also pass a lambda function
        # 'words': RunnableLambda(lambda x: len(x.split()))

    }
)

res = RunnableSequence(joke_chain, parallel_chain)

print(res.invoke({'topic': 'AI'}))