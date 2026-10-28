# RAG (Retrieval Augmented Generation) pipeline core components that are used to connect data with LLMs:

- Document Loader

- Text Splitter

- Vector Store

- Retrievers


# What is RAG?

Query(Prompt) --->  LLMS --->  Response


# LLMS:

LLMS are AI model trained on vast amounts of text data to understand, generate, and process human language. (It is also known as Parametrix knowledge becuase it store data in parameters in number vector form) and we access that data through prompting(Query) 


# There are three limitations in prompting through which we can't access data from LLMs paramters:

1) Private data - LLMs cant answer on my personal data

2) Recent data - LLMs cant answer on current data because it answer on pretrained model

3) Hallucination - LLMs give wrong answer with surity even if they dont know answer in some situation


# First Solution:

Fine-tuning - In fine tuning we take pretrained model and again train on smaller specific domain dataset 


# How to do fine-tuning:

- Supervised Fine-tuning (SFT) - In which we provide (prompt + desired output) in labeled dataset so that if user ask that question then you provide desired output 

- Domain Specific Fine-tuning (DSFT) - It is also known as continued pretraining becuase in which we pretrained model on a smaller domain specific dataset

- Reinforcement Learning from Human Feedback (RLHF): It uses human ratings of model answers to train a reward signal that guides the LLM


# Supervised Fine-tuning:

- Collect data - labeled dataset (prompts + desired output)

- Choose a method - LoRA/QLoRA

- Train for a few epochs - keep the base weights frozen and update only a small subset or all weights

- Evalute & safety-test - Measure exact-match, factuality, and hallucination rate against held-out data, red-team for safety


# Disadvantage of Fine-tuning:

- Computation Cost - Train large model is cost computating

- Technical Expertise - You need proper AI engineer to do fine-tuning

- Data Recency - Frequent new information because data outdate quickly

- Overfitting - If trained on a small dataset for too long, the model will memorize the training data rather than learning general patterns


# Second Solution:

In Context Learning - It is a core capability of LLMS like GPT-3/4, CLaude, and Llama where the model learns to solve a task by seeing examples in the prompt wihtout updating its weights.

It is a emergent property of LLMs

Architecture:

Query (prompting) + In Context Learning  --->  LLM  --->  Response

- Instead of just example task, retrieve background information, facts, documents, product manuals, etc.

- Inject that into the prompt to augment(merge query(prompting) with extra information of that content) the model's knowledge

example->

"""

You are a helpful assistant.

Answer the uestion ONLY from the provided context.

If the context is insufficient, just say you don't know.

{context}

Question: {question}

"""


# Now enhance In Context Learning that is basically RAG:

Instead of adding example in prompt we provide context(required knowledge) with query(prompt) to LLMs so that it give desired response

RAG is a way to make a LLMs model (like ChatGPT) smarter by giving it extra information (context) at the time you ask your question

Workflow

Query + Context  -->  LLM  -->  Response

explanation ->  to solve a query, we inject all the required knowledge directly into the prompt before sending it to the LLMs so that it gives desired output


# Understanding RAG:

there are four step of making RAG based system:

- Indexing - it is a process of create external knowledge base that is derived context

- Retrieval - it retrieve that chunks/part from external knowledge base (context) which is required in query/prompt

- Augmented - it merge that retrieve chunks with query to make final query

- Generation - then LLMs process this final query with the help of parameters and this context to answer this query and generate desired response


# Indexing Process:

- Document Ingestion - Fetch/load your source knowledge(like web video transcripts, AWS S3 Service) into memory(like pdf report, doc file, sql records) through different tools(like LangChain loaders (PyPDF Loader, YoutubeLoader, WebBaseLoader, GitLoader))

Now that source knowledge is stored in a document string

- Text Chunking - Break large documents into small meaningful chunks through different tools(like RecursiveCharacterTextSplitter, SemanticChunker)

- Embedding Generation - Convert each chunk into a dense vector(embedding) through Embedding Models(like OpenAIEmbeddings, SentenceTransformerEmbeddings) that captures its meaning and it helps in to store semantic meaning of that chunks docs and we do this because semantic searching happens in between embedding vectors

- Storage in a Vector Store - We store that vectors along with original chunks text + metadata in a vector database and we can used that vector store as external knowledge base

Vector DB:

Local - FAISS, Chroma

Cloud - Pinecone, Weaviate, Milvus, Qdrant


# Retrieval Process:

It is a process of finding the most relevant pieces of information from a pre-build index(created during indexing) based on the user's question

Step-1 -> Retriever generate embedding vectors for that query through same Embedding Model

Step-2 -> In which we perform semantic search on embedding vectors to reach closes vector

Step-3 -> Perform ranking on that relevant close vectors

Step-4 -> Fetch chunks from that top ranking vectors

# Augmentation Process:

In which we merge that chunks with query so that when we provide final query (query + relevant chunks) to the LLMs and if the context is insufficient, just say you dont know

# Generation Process:

It is a final step where a LLMs uses the user's query and the retrieved & augmented context to generate a response


# RAG Complete Pipeline:

![alt text](.\images\rag_pipeline.png)

# Conclusion:

RAG is a cheaper solution than Fine-tuning becuase it dont need to train model and dont need any proper label dataset becuase it simply implement based on web source information