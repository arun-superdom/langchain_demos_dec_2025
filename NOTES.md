# AI — Overview

This document contains concise notes on Artificial Intelligence (AI) covering key categories, core technologies, and tooling. These notes are organized into sections and include brief explainers where useful.

---

## What is AI?
AI (Artificial Intelligence) is the field of computer science focused on building systems that perform tasks typically requiring human intelligence — such as perception, decision-making, and language understanding.

## Types of AI
AI is commonly categorized into two broad types in everyday usage: Narrow/Traditional AI and Modern (Generative) AI.

### Narrow AI (Traditional / Discriminative AI)
- **Definition:** Narrow AI systems are designed to perform specific tasks such as classification, prediction, detection, or recommendation.
- **Deterministic outputs:** Given the same input and environmental conditions, many narrow AI models will return the same output. They are typically optimized for accuracy and stability.

**Common examples:**
- Spam detection in email
- Fraud detection in banking
- Product recommendation engines in e-commerce
- Image recognition
- Speech recognition
- Natural Language Processing (task-specific models)

**Technology / Typical workflow:**
1. Dataset collection and preprocessing
2. Train a machine learning model on labeled data
3. Validate the model on held-out datasets
4. Test the model to measure generalization
5. Deploy the model to production

> Note: Narrow AI focuses on solving a well-defined problem reliably. The model's objective and evaluation are usually quite specific.

---

### Modern AI (Generative AI)
- **Definition:** Generative AI systems are built to generate new content — text, images, audio, video, or code — rather than only classifying or predicting pre-existing categories.
- **Stochastic outputs:** Generative models are often non-deterministic; they may produce different outputs for the same prompt unless randomness is controlled (e.g., using a fixed seed or temperature).

**Common examples and applications:**
- ChatGPT, Anthropic Claude, and Google Gemini (text-based conversational agents)
- DALL·E, Midjourney, Stable Diffusion (image generation)
- Music generation tools like AIVA, Jukedeck
- Video synthesis and avatar-based video generation tools
- Code generation such as GitHub Copilot

**Technology:**
- Large Language Models (LLMs) are the dominant technology in modern generative AI. These models learn from large corpora of unstructured or semi-structured data and are often fine-tuned for particular tasks.
- Multi-modal models can process and generate across modalities (e.g., text + images).

**Capabilities:**
1. **Thinking / Reasoning** — LLMs can show limited reasoning and chain-of-thought behavior; they are best with well-structured prompts and constraints.
2. **Tool Calling / Function Calling** — Modern models can be designed to call external tools or APIs to fetch updated data or perform side effects (e.g., web search, database queries, or code execution).
3. **Multimodality** — Models that accept and produce text, images, and audio enable complex pipelines for creative or assistive tasks.

**Types of Generative Models:**
- **Closed-source LLMs:** e.g., ChatGPT (OpenAI), Google Gemini, Anthropic Claude. These are typically fully managed and hosted by their providers.
- **Open-source LLMs:** e.g., LLaMA variants, Qwen, Gemma, Grok (open-source versions), and other community forks and models. These allow local deployment and customization.

> Tip: You can often make generative outputs more predictable by lowering sampling temperature, using beam search, or re-running prompts with controlled randomness.

---

## AI Agents & AI Coding Agents
- **AI Agent:** An AI system that can autonomously understand tasks, plan, take actions, verify outcomes, and iterate to reach a goal. Agents combine reasoning, memory, and tools.

- **AI Coding Agent:** A specialized agent that helps writing, refactoring, or completing code — from simple autocompletion to complex multi-file code generation and maintenance.

**Editor-based AI coding agents:**
- GitHub Copilot (VS Code, JetBrains plugins) — completions and suggestions while coding
- Cursor — in-editor AI for code comprehension and generation
- Windsurf, Cline, Kiro, Supermaven — other IDE and extension-based coding agents

**CLI / Autonomous code agents:**
- Claude Code, OpenAI Codex-based implementations, Google Gemini CLI — provide higher-level code generation or automation from the command line or scripting environments.

> Note: AI coding agents can accelerate development but still need human oversight — review suggested code for correctness, security, and style.

---

## Quick Tips & Best Practices
- Prefer narrow models or task-specific fine-tuning for high-accuracy, deterministic tasks (e.g., fraud detection).
- For tasks requiring creativity or multi-modal outputs, use generative models and add guardrails, prompts, and tools for verification.
- Always validate model behavior with test data and monitor deployed models for drift and bias.

---

## Further reading & Tools
- OpenAI, Anthropic, Google AI research pages
- Hugging Face for open-source models and datasets
- Papers and tutorials on LLM fine-tuning and tool integration

---


python3 -m venv .venv
source .venv/bin/activate
pip3 install python-dotenv


pip install pyautogen python-dotenv
pip install -U "autogen-agentchat" "autogen-ext[openai]"


1. Basic single agent - Simple task execution
2. Tool integration - Adding custom functions as tools
3. Multi-modal input - Working with images
4. Two-agent interaction - Basic multi-agent patterns
5. Structured output - Using Pydantic models for typed responses
6. Streaming - Real-time token output
7. Multiple tool iterations - Complex reasoning chains


Advanced concepts
8. Round Robin Teams - Agents take turns in fixed order with reflection pattern
9. Selector Group Chat - AI-driven speaker selection based on context
10. Custom Memory Management - Control conversation history per agent
11. Agent-as-Tool - Using specialized agents as callable functions
12. Sequential Handoffs - Workflow with explicit handoff between stages
13. External Control - Stopping teams externally and cancellation
14. State Management - Resuming conversations and managing team state



Building Blocks of AutoGen 
===
  Agents
  Models
  Tools
  Terminations

Key features of AutoGen 
====
  1. Asynchronous Messaging
  2. Scalable & Distributed
  3. Multi-Language Support
  4. Modular & Extensible
  5. Observable & Debuggable
  6. Event-Driven Architecture



AI Agent Patterns
====
  1. Tool Use Pattern 
      (example2)
      AI agents can identify and call tools to connect to external apis, databases, etc.

  2. Reflection Pattern 
      (example9)

      AI Agents evaluate AI agent's own output and reflect -- till it arrives at final response

  3. Agent as Tool Pattern 
      (example11)

      Sometimes tools should connect to LLM (example scenario: for fact checking)

  4. ReAct (Reasoning + Act) Pattern 
      Agent must show reasoning steps and then act. So that transparency is achieved 
      about decision making.

  5. Multi-Agent Pattern
      Some complex problems can be fixed when multiple agents aligned to 
      complete the tasks

  6. Planning Pattern 
      Agent will decompose the complex steps into small sub steps 
      



AI Agent Processes
===
    1. Sequential
    2. Hierachical
    3. Hybrid 
    4. Parallel
    5. Async



MCP 
===
  Model Context Protocol 
  1. MCP Server
      For example [Gmail MCP Server]: 
        tool1,
        tool2, 
        tool3
        ..
        tool50

  2. MCP Client 
      * will connect to AI agents 


3 Core Concepts
==
  MCP servers can provide three main types of capabilities:
  #1 Resources: File-like data that can be read by clients (like API responses or file contents)
  #2 Tools: Functions that can be called by the LLM (with user approval)
  #3 Prompts: Pre-written templates that help users accomplish specific tasks

3 Ways to Connect to MCP Servers
-----
  1. STDIO (only for accessing resources from local computer)
    * only local server connections are possible 

  2. Http with Server Side Events (SSE)
    * remote mcp server connections are possible

  3. Streamable Http [RECOMMENDED]
    * most advanced 
    * use this in production

To have persistent connection with http you have 2 options
--- 
  1. Server Side Events (SSE)
  2. Websockets



_File updated and organized for clarity — end of notes._
