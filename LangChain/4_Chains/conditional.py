from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableParallel,RunnableLambda, RunnableBranch


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

class Feedback(BaseModel):
    sentiment: Literal['Positive', 'Negative']= Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)
 
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback}\n {format_instruction}",
    input_variables= ['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback\n{feedback}",
    input_variables= ['feedback'],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback\n{feedback}",
    input_variables= ['feedback'],
)

classifier_chain  = prompt1|model|parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment =='Positive',prompt2|model|parser),
    (lambda x:x.sentiment =='Negative',prompt3|model|parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain|branch_chain
result = chain.invoke({'feedback':'This is a beautiful product'})

print(result)

chain.get_graph().print_ascii()

