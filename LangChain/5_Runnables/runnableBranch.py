# Used for creating conditional branches in the runnable tree

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableBranch, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables= ['topic']
)

prompt1 = PromptTemplate(
    template = "Summarize the following text - {response}",
    input_variables= ['response']
)

report_chain = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt1, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain, branch_chain)

print(final_chain.invoke({'topic': 'AI'}))