# Let's build weather agent
from dotenv import load_dotenv
import os
import requests
from langchain.agents import create_agent
load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    # Let's use openweathermapapi for this example
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return "API key for OpenWeatherMap is not set."
    
    WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(f"{WEATHER_API_URL}?q={city}&appid={api_key}&units=metric")
    weather_data = response.json()
    current_weather = weather_data.get("weather", [{}])[0].get("description", "unknown")
    temperature = weather_data.get("main", {}).get("temp", "unknown")

    return f"The current temperature in {city} is {temperature}°C."

agent = create_agent(
    model="gpt-4o-mini",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in Sydney?"}]}
)

print(result["messages"][-1].content)

