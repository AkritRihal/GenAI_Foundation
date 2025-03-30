from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain.schema.runnable import RunnableParallel


load_dotenv()

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables= ['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions and Answers from the following text \n {text}",
    input_variables= ['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided quiz and notes into a single document \n notes->{notes} quiz->{quiz}",
    input_variables= ['notes', 'quiz']
)

model2 = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    # task = "text-generation"
)
model1 = ChatHuggingFace(llm = llm )

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes":prompt1|model1|parser,
    "quiz":prompt2|model2|parser
})

merge_chain = prompt3|model2|parser

chain = parallel_chain|merge_chain

text = """
The first AI was called the Logical Theorist, developed in 1956 by Allen Newell
and Herbert Simon. It was a program that could reason and solve problems
using logical deduction. The first AI program that could learn from experience
was called the General Problem Solver, developed in 1969 by John McCarthy.
The first AI program that could understand natural language was called
ELIZA, developed in 1966 by Joseph Weizenbaum.
"""

result = chain.invoke({"text": text})
print(result)
chain.get_graph().print_ascii()