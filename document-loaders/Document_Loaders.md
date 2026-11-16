# Document Loader:

It is a component in LangChain used to load data from various sources into a standardized format (usually as Document objects), which can then be used for chunking, embedding, retrieval, and generation.

Document object format:

```
Document(
    page_content="The actual text content",
    metadata={"source": "filename.pdf", ...}
)
```



# Types of Document Loaders:

- TextLoader
- PyPDFLoader
- DirectoryLoader
- WebBaseLoader
- CSVLoader



## (1) TextLoader:

It is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects.


### Use Cases:

Ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.

Ex-> YouTube video transcript


### Limitation:

Works only with .txt files



## (2) PyPDFLoader:

It is document loader in langchain used to load content from PDF files and convert each page into a Document objects.

```
[
    Document(page_content="Text from page 1", metadata={"page": 0, "source": "file.pdf"}),
    Document(page_content="Text from page 2", metadata={"page": 1, "source": "file.pdf"}),
    ...
]
```


### Use Cases:

- If simple and clean PDFs then use PyPDFLoader
- If PDFs with tables/column then use PDFPlumberLoader
- If Scanned/image PDFs then use UnstructuredPDFLoader or AmazonTextractPDFLoader
- If you need to extract layout and image data then use PyMuPDFLoader
- If you want best structure extraction then use UnstructuredPDFLoader


### Limitations:

It uses the PyPDF library under the hood, not great with scanned PDFs (made pdf by images) or complex layouts



## (3) DirectoryLoader:

It is a document loader that lets you load multiple documents from a directory/folder of files

```
Glob Pattern                      What it Loads

"**/*.txt"                        All .txt files in all subfolders
"*.pdf"                           All .pdf files in the root directory
"data/*.csv"                      All .csv files in the data/ folder
"**/*"                            All files (any type, all folders)

**   =   recursive seaarch through subfolders
```



## (4) WebBaseLoader:

It is a document loader in LangChain used to load and extract text content from web pages (URLs)


### Use Cases:

For blogs, news articles, or public websites where the content is primarily text-based and static

### Limitations:

- It does not handle JavaScript-heavy pages well and for that you need to use SeleniumURLLoader
- It loads only static content (what's in the HTML, not what loads after the page renders)



## (5) CSVLoader:

It is a document loader used to load CSV files into LangChain Document objects, one per row, by default



# Problem of Loading Documents through `load()` Function:

In document loaders, the `load()` function extracts and loads all documents into memory at once, which slows down execution and risks overflowing RAM when dealing with large files or huge datasets. To solve this, `lazy_load()` loads documents one by one on demand (as a generator), preventing memory overload and ensuring efficient processing.


## Load vs Lazy Load:

### load():

- Eager loading (loads everything at once)
- Return a list of Document objects
- Loads all documents immediately into memory
- It is best when:
The number of documents is small and you want everything loaded upfront


### lazy_load():

- Lazy Loading (loads on demand)
- Return a generator of Document objects
- Not all documents are loaded at once, they are fetched one at a time as needed
- It is best when:
You are dealing with large documents or lots of files and you want to stream processing (e.g., chunking, embedding) without using lots of memory



# Custom Document Loader:

You can also create your own document loader by creating class like ->

```
class CustomDocumentLoader(BaseLoader):
    """An example document loader that reads a file line by line."""

    def __inti__(self, file_path: str) -> None:
        """Initialize the loader with a file path."""

    # In our custom document loader we can use any load function
    def lazy_load(self) -> Iterator[Document]:
        """A lazy loader that reads a file line by line."""

        """Through our custom logic we can create our custom document loader"""
```