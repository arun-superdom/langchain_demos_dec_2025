from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import requests

load_dotenv()

# Use OpenAI as the model 
# use this when you want to control model parameters more finely
model = ChatOpenAI(
    model="gpt-5.1",          # Fast and cost-effective with great tool calling
    temperature=0,                # Deterministic for agent use
)

# let create web search tool -- which uses https://serper.dev/ SerpAPI
@tool 
def web_search_tool(query: str) -> str:
    """Perform a web search to gather current information on a topic/query."""
    print("========= Web Search Tool Invoked ============")
    
    import os
    
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return "Error: SERPER_API_KEY not found in environment variables"
    
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {"q": query}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        results = response.json()
        
        # Extract organic search results
        organic_results = results.get("organic", [])
        search_summary = []
        for idx, result in enumerate(organic_results[:5], 1):  # Get top 5 results
            title = result.get("title", "")
            snippet = result.get("snippet", "")
            search_summary.append(f"{idx}. {title}: {snippet}")
        
        return "\n".join(search_summary) if search_summary else "No results found"
    
    except requests.exceptions.RequestException as e:
        return f"Error performing web search: {str(e)}"


# ---- Define specialized sub-agents ----
# Research Agent: searches or retrieves information
research_agent = create_agent(
    model=model,
    tools=[web_search_tool],
    system_prompt="You are a research assistant. Provide detailed, factual information on any topic by doing web searches when necessary.",
)

# Let's expose this research agent over a tool
@tool
def call_research_agent(query: str) -> str:
    """Call the research agent to gather information on a topic/query."""
    print("========= 1. Planning to invoke research agent ============")
    result = research_agent.invoke({
        "messages": [{"role": "user", "content": query}]
    })
    return result["messages"][-1].content

# Writing Agent: writes or summarizes content
writing_agent = create_agent(
    model=model,
    tools=[],
    system_prompt="You are a professional writer. Create clear, concise, and engaging content.",
)

# Lets expose this writing agent over a tool
@tool
def call_writing_agent(query: str) -> str:
    """Call the writing agent to write or summarize content."""
    print("========= 2. Planning to invoke writing agent ============")
    result = writing_agent.invoke({
        "messages": [{"role": "user", "content": query}]
    })
    return result["messages"][-1].content

# ---- Define supervisor agent ----
supervisor_agent = create_agent(
    model=model,
    tools=[call_research_agent, call_writing_agent],
    system_prompt=(
        "Today is 15th Dec 2025. You are a supervisor agent. You coordinate tasks between specialized agents:\n"
        "First ask the research agent to gather necessary information. Finish this first and then go on to writing\n"
        "- Use call_research_agent for research and information gathering.\n"
        "- Use call_writing_agent for writing, editing, or summarizing.\n"
        "Delegate tasks to the appropriate agent and combine their outputs to answer the user."
    ),
)

# ---- Run the multi-agent system ----
if __name__ == "__main__":
    user_task = "Research Virat Kohli's form in recent cricket matches in 2025 and write a 4-paragraph summary. Also give stats about his performance in recent times."
    
    print("========= 0. Planning to invoke supervisor agent ============")
    result = supervisor_agent.invoke({
        "messages": [{"role": "user", "content": user_task}]
    })
    
    print("=== Supervisor's Final Response ===")
    print(result["messages"][-1].content)
