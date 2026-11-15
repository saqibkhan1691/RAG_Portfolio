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
- WebBaseLoader
- CSVLoader

