from langchain_community.document_loaders import CSVLoader


loader = CSVLoader(file_path='documents/subscription.csv')


docs = loader.load()


print(len(docs))    ## it return no. of rows in csv


print(docs[0])     ## it return first row of csv