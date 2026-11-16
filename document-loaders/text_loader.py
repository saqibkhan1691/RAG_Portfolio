# All document loaders are available in langchain_community
# Loads text files as LangChain documents
from langchain_community.document_loaders import TextLoader


# Initialize TextLoader with UTF-8 encoding to ensure all characters are read properly without decoding errors
loader = TextLoader('documents/cricket.txt', encoding='utf-8')


# It load text file as a document
docs = loader.load()


print(docs)


print(type(docs))    ## <class 'list'>


print(len(docs))     ## 1


print(type(docs[0]))   ## <class 'langchain_core.documents.base.Document'>


print(docs[0])     ## print document in document_object format (page_content, metadata)


print(docs[0].page_content)     ## print page_content of document


print(docs[0].metadata)         ## print metadata of document





## Load a text document, format it into a prompt, and generate a summary using an OpenAI LLM chain

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
# Converts AI response into a plain string
from langchain_core.output_parsers import StrOutputParser
# Creates dynamic prompts with placeholders/variables
from langchain_core.prompts import PromptTemplate
# Imports function to read .env file
from dotenv import load_dotenv


# Loads API keys from .env into environment variables
load_dotenv()


model = ChatOpenAI()


prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)


parser = StrOutputParser()


loader = TextLoader('documents/cricket.txt', encoding='utf-8')


docs = loader.load()


chain = prompt | model | parser


result = chain.invoke({'poem': docs[0].page_content})

print(result)