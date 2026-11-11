# Text Splitting:

It is a process of breaking large chunks of text into smaller pieces (chunks) that an LLM can handle effectively.


## Text Splitter:

The process of doing this is text splitter.


## Main reason of text splitting:

Many embedding models and language models have maximum input size constraints where splitting allows us to process document otherwise exceed these limits.

Text splitting improve LLM powered task like -> Embedding, Semantic Search, Summarization

- Embedding - Short chunks yield more accurate vectors

- Semantic Search - Search results point to focused info, not noise

- Summarization - Prevents hallucination and topic drift


## Optimizing Computational resources:

Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks.



# Types of Text Splitters:

(1) Length Based

(2) Text Structure Based

(3) Document Structure Based

(4) Semantic Meaning Based

## (1) Length Based:

In length based we split the text based on size for example size=100 it means after 100 character chunk 2 will start then next 100 characters chunk 3 will start and so on

![Length Based](.text_splitters/image/length_based_text_splitting.png)


## (2) Text Structured Based:

In this we split the text by paragraph, sentence, word, character and it try splitting first by paragraph if that is not possible then sentence if sentence wise not possible then word wise then character 

- \n\n -> paragraph

- \n   -> sentence

- _    -> word

- ''   -> character

example -> 

![Text Structured Base](.text_splitters/image/text_structured_base.png)



## (3) Document Structure Based:

In divides a document into smaller chunks by following its natural layout like headings, paragraphs, code blocks, or pages, rather than cutting text off at random character limits.



## (4) Semantic Meaning Based:

It split the text my meaning of text (like -> topic_1, topic_2, topic_3, etc) not by text structure because rest splitters fail if multiple topics discuss in single paragraph

It breaks the document into smaller base units, usually sentences then calculates vector embeddings for each sentences to capture its core meaning through embedding model then compare semantic similarity between consecutive sentences and it creates chunk boundary whenever there is a significant shift in meaning between sentences