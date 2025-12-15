
2 Ways to use LLMs
=====
  1. cloud version (chatgpt.com, gemini.google.com, grok.com)
  2. via APIs (OpenAI API, Gemini API, Grok API).  [WE WILL TRY THIS APPROACH TO BUILD AGENTS]


# AI Agents
---
  Python, JavaScript (Vercel AI SDK, Langchain JS), DotNet (SemanticKernel)


2 Types of AI Agents
====
  1. Autonomous Agents 
  2. Semi-autonomous / Human-in-the-loop (HITL) Agents 



3 Ways to build AI Agents
===
  1. No Code Tools (n8n / langflow)
  2. Low Code Tools (LangGraph)
  3. With code (Agent Development Frameworks)

## AI Agent Development Frameworks
---
  ### Python-based 
  ----
    1. LangChain (also available as JS package)
        previous versions < 1.0 (complex for devs to learn)
        current version > 1.0 (easier for us to learn)
    2. Autogen
    3. CrewAI
    4. LlamaIndex
    5. Agno
  
  ### JS-Based 
    1. Vercel AI SDK
    2. LangChain JS




## LangChain 
===

### Core Building Blocks of AI agents
---
  1. LLM with Reasoning Capability / LLM tuned for AI Agents
  2. Prompts  (preferred: ReAct)
  3. Tools / Functions / Integrations / MCP (WebSearch, Weather)
  4. Knowledge Base (optional)
  5. Memory (third party tools)
  6. Guardrails (third party tools)
  7. Observability (Evaluate AI Agent)



### AI Agents vs Agentic AI
AI Agents are single agents 
Agentic AI is multi-agent system

=====

## Components of Langchain 
1. Chat models [DONE]
2. Messages [DONE]
3. Prompt templates [DONE]
4. Example selectors
5. LLMs [DONE]
6. Output parsers [DONE]
7. Document loaders
8. Text splitters
9. Embedding models
10. Vector stores
11. Retrievers 
12. Tools [TODO]
13. Agents [TODO]
14. Multimodal
15. Indexing 


Agents
===
  Requirement 
    * our agent listens to users queries related to weather and answers 
    * should we address queries outside the original scope? no 

Tools 
===
  * simple function that does something 
  * must have name and description [this needs to have clarity] properties 
  * must return value
  * description is a prompt for the tool 
  * function arguments are optional



Types of AI Agents
--
  1. Autonomous 
  2. Semi-Autonomous


Factors to consider when we build AI Agents
---
  1. Does the model have reasoning capability?
  2. Can the model perform the tool calls / function calls
  3. Context window 


====
2 Approaches 
---
  Single Agent with many tools 
    1. get_user_location
    2. get_date
    3. get_weather
    4. get_weather_forecast
    5. book_turf 
    6. make_payment
    7. send_notification_for_otp
    8. get_otp 
    9. send_booking_confirmation
  Many tiny agents with individual tools 
    1. userInfoCollector agent 
        1. get_user_location
        2. get_date
        3. get_weather
        4. get_weather_forecast

    2. bookingAgent 
        1. book_turf 
        2. make_payment
        3. get_otp 

    3. NotifierAgent 
        1. send_notification_for_otp
        2. send_booking_confirmation





Types of Databases
===
  1. RDBMS 
      Examples: Oracle, MySQL, Postgres, MariaDB, MS-SQL Server

      select * from students where first_name=john

  
  2. NoSQL 
      Example: MongoDB 

      students.findAll({first_name: "John"})

    
  3. Vector Databases 
      Examples: PineCone, ChromaDB, Qdrant, Milvus, Weaviate, Pg-vector

      vector querying ? 


===
Steps to following to embed data into vector db
===
  1. Have the PDF e-book (or any other file type also)
  2. Check for the data inside PDF e-book
      2.1 if the texts are selectable -- use text extractor [Let's follow this one]
      2.2 if the texts are with images -- use image processing tools + text extractor 
      2.3 if the texts are of scanned book (you can't select the text) -- OCR tools 

  3. after you extract the text -- implement good chunking strategy
      3.1 decide on how many token per chunk (ex: 800)
      3.2 decide on how many token of chunk overlap (ex: 200)
      3.3 use the embedding model to embed 
      3.4 connect to vector db using vector db client and store the embeddings 
  
  4. Build the retrieval logic 
      4.1 get the text from chatbot 
      4.2 use the embedding model and convert this text to embeddings 
      4.3. for that embedding - do a semantic search 
      4.4 get the answer and send it to llm 
      4.5 llm will augment and respond to the user 


AI agents can call tools autonomously.
Tools:
===
  * tools are functions in python
  * function must have a name
  * function must have description
  * function must return data
  

def hello(name: str): str
  """tool that greets user by name"""
  return "Hey!" + name 




AI Agents - Design Patterns
====
  1. Reflection
  2. Tool Use Patterns (Agent as a tool)
  3. ReAct Pattern 
  4. Multi-Agent Pattern 
  5. Planning Pattern