# Why we need Vector Stores?

A Vector Store is a specialized database that saves data as numerical vectors to search information based on meaning and context rather than exact keywords. It acts as an external memory for AI models in RAG pipelines, using similarity math to quickly pull up the most relevant unstructured data like text, images, or audio

# Note:

Text is passed through a Neural Network (Embedding Model), which captures its semantic context and converts it into a high-dimensional numerical array called a Vector Embedding. These vectors are then stored in the Vector Store for fast similarity search.

![Embedding Vectors](.vector-stores/images/embedding_vectors.png)



# Challenges in making this type of system:

- Generate embedding vector for every text suppose if you have millions of text then you need to generate millions of embedding vectors

- You need different type of database to store these mebedding vector (not RDBMS)

- For semantic search you need to compare each vector to get closes vector and if millions of vectors then you need to compare millions of vector to reach closes vector



# Solution for these challenges:

Vector Store or Vector Database



# Vector Stores:

It is a system designed to store and retrieve data represented as numerical vectors.



# Key Features:

- Storage - it ensures that vectors and their associated metadata are retained (we can store both metadata and embedding vectors), whether in-memory for quick lookups or on-disk for durability and large-scale use.

- Similarity Search - it helps to retrieve the vectors which is most similar to a query vector.

- Indexing - A process that organizes vector embeddings into efficient structures (like clusters or trees) using algorithms such as HNSW or IVF. Instead of comparing a query against every single vector, it narrows down the search space to speed up similarity lookups. (e.g. approximate nearest neighbor lookups)

- CRUD Operations - Manage the lifecycle od data (adding new vectors, reading them, updating existing entries, removing outdated vectors)



# Use Cases:

- Semantic Search

- RAG

- Recommendation Systems

- Image/Multimedia search



# What is the  difference between Vector Store and Vector Database?

## Vector Store:

- It typically refers to a lightweight library or service that focuses on storing vectors(embeddings) and performing similarity search (retrieval).

- It may not include many traditional database features like transactions, rich query languages, ACID properties

- Ideal for prototyping, smaller-scale applications.

- Example -> Chroma, FAISS (where you store vectors locally and can query them by similarity, but you handle persistance and scaling separately)


## Vector Database:

- A full-fledged database system designed to store and query vectors.

- If you can add additional features with vector store system then it is vector database

Additional Features:

- Distributed architecture for horizontal scaling

- Durability/ Backup and restore if data loss in future

- ACID transactions

- Concurrency means multiple user can communicate with database

- Authentication for securing database 

Examples -> Pinecone, Milvus, Qdrant, Weaviate


### CONCLUSION:

A vector database is effectively a vector store with extr database features (e.g -> clustering, scaling, security, metadata, filtering, and durability)

(Vector store is a subset of vector Database)



# Chroma Vector Store:

![Chroma Vector Store](.vector-stores/images/chroma_vector_store.png)