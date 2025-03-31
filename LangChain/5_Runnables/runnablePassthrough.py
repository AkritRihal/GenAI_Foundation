# returns same output , does not do any modification, 
# returns input as output

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Generate a joke on {topic}",
    input_variables= ['topic']
)

prompt1 = PromptTemplate(
    template = "Explainn  the following - {response}",
    input_variables= ['response']
)

joke_chain = RunnableSequence(prompt, model, parser)


parallel_chain = RunnableParallel(
    { 
        'joke': RunnablePassthrough(),
        'explanation': RunnableSequence(prompt1,model, parser)
    }
)

res_chain = RunnableSequence(joke_chain, parallel_chain)

print(res_chain.invoke({'topic': 'AI'}))