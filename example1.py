# Load the environment variables from the .env file
from dotenv import load_dotenv
import os
load_dotenv()

# Now let's create a simple agent 
from langchain.agents import create_agent
from langchain.tools import tool

# Define a simple tool to greet
@tool
def greet(name: str) -> str:
    """Greet a person by name."""
    print(f"Greeting {name}")
    return f"Hello, {name}!"

agent = create_agent(
    model="gpt-4o-mini",
    tools=[greet],  # register the tool
    system_prompt="""You are a helpful assistant.""",
)

response = agent.invoke(
 {
    "messages": [{  
      "role": "user", 
      "content": "What tool do you have access to?"
    }]
  }
)

# print(response)
print(response["messages"][-1].content)