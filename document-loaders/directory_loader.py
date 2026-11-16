# it used to extract complete folder with their pdf files in document object
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',     ## path of folder
    glob='*.pdf',     ## it means load every pdf files from books folder
    loader_cls=PyPDFLoader
)


docs = loader.load()

# docs = loader.lazy_load() 


print(docs)


print(len(docs))      ## it return total no. of pages of each pdf file