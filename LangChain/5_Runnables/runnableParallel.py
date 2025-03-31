from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template = "Genearte a tweet about {topic}",
    input_variables =['topic']
)

prompt2 = PromptTemplate(
    template = "Genearte a linkedin post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()
model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

chain = RunnableParallel({
    'tweet': RunnableSequence(prompt, model, parser),
    "post": RunnableSequence(prompt2, model, parser)
})

res = chain.invoke({'topic': 'AI'})
print(res["tweet"] ,"\n")
print(res["post"])
