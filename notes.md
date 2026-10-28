# RAG pipeline core components that are used to connect data with LLMs:

- Document Loader

- Text Splitter

- Vector Store

- Retrievers


# What is RAG?

Query(Prompt) --->  LLMS --->  Response


# LLMS:

LLMS are AI model trained on vast amounts of text data to understand, generate, and process human language. (It is also known as Parametrix knowledge becuase it store data in parameters in number vector form) and we access that data through prompting(Query) 


# there are three limitations in prompting through which we can't access data from paramters:

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


