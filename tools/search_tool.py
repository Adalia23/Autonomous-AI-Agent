from langchain_core.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

@tool
def search_tool(query: str) -> str:
    """Search the web for current information on any topic."""
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = client.search(query=query, max_results=5)
    results = response.get("results", [])
    output = ""
    for r in results:
        output += f"- {r['title']}: {r['content'][:300]}\n\n"
    return output or "No results found."