from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('documents/sample.pdf')

docs = loader.load()

print(docs)
print(docs[0].page_content)