recommended version for langchain v1 (as of 15th dec 2025) is python v3.13 


commands to try first
  python --version (ensure you have 3+) or python3 --version
  pip --version  or pip3 --version 

Creating virtual environment (do it only once)
  python -m venv .venv or python3 -m venv .venv

Activating virtual environment in Mac 
  source .venv/bin/activate 

Activating virtual environment in Windows 
  .venv\Scripts\activate 

Install lanchain packages via pip 
  pip install -U langchain langchain-openai 
  or
  pip3 install -U langchain langchain-openai 


To load .env inside our project 
  pip install python-dotenv 
  or
  pip3 install python-dotenv 


python multi_agent_example2.py 
==========


Next 2 Examples 
===
  Simple Multi-Agent System
  
  RAG System Project
  ======
    1. ingestion.py  
        * we will use chromadb (vector db)
        * we need to have .pdf (data/HR_policy.pdf)
        * chunking strategy (hor many token of text, chunk overlap)
        * embedding model 
        * connect to vector db 
        * store the vector embeddings with meta data

    2. retrieve.py 
        * 


