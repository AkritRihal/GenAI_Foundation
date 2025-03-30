from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on  {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template  =" Generate a 5 pomint summary from following text \n {topic}",
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

parser = StrOutputParser()

chain = prompt1|model|parser|prompt2|model|parser

result = chain.invoke({'topic':'Himachal Pradesh'})

print(result)

chain.get_graph().print_ascii()
