from langchain_text_splitters import CharacterTextSplitter

# Load text from file where PyPDFLoader is used to load the text from a PDF file
from langchain_community.document_loaders import PyPDFLoader

# Load the PDF file using PyPDFLoader
loader = PyPDFLoader('./documents/sample_text_splitting.pdf')

## it returns list of Document objects, each Document object contains the text of a page in the PDF file
docs = loader.load()



# text = """
# The impact of artificial intelligence (AI) on various sectors has been profound and transformative. In healthcare, AI has revolutionized diagnostics and treatment planning, enabling faster and more accurate identification of diseases. Machine learning algorithms can analyze vast amounts of medical data, leading to personalized treatment plans and improved patient outcomes. In the financial sector, AI-driven algorithms enhance fraud detection, automate trading, and provide personalized financial advice, thereby increasing efficiency and security.
# """



splitter = CharacterTextSplitter(
    chunk_size=100,      ## Specify the maximum number of characters in each chunk
    chunk_overlap=20,    ## Specify the number of characters to overlap between chunks and 10-20 characters is a good range to use
    separator=''         ## Specify the separator to use when splitting the text
)

## result = splitter.split_text(text)
result = splitter.split_documents(docs)



## it return list of strings, each string is a chunk of the original text
print(result)

## No. of chunks created
print(f"Number of chunks created: {len(result)}")

## retrieve the first chunk of text
print(result[0].page_content)