from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/product/p/item?pid=COMHH6Q4E6HYUURM&PARAM=3738&BU=CoreElectronics&pageUID=1794853816471"
loader = WebBaseLoader(url)


docs = loader.load()


print(len(docs))

print(docs[0].page_content)





## Load a webbase document through URL, format it into a prompt, and generate a summary using an OpenAI LLM chain

from langchain_community.document_loaders import WebBaseLoader
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
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)


parser = StrOutputParser()


url = "https://www.flipkart.com/product/p/item?pid=COMHH6Q4E6HYUURM&PARAM=3738&BU=CoreElectronics&pageUID=1794853816471"
loader = WebBaseLoader(url)


docs = loader.load()


chain = prompt | model | parser


result = chain.invoke({'question':'What is the product that we are talking about?', 'text': docs[0].page_content})

print(result)