import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.search_tool import search_tool
from tools.calculator_tool import calculator_tool
from tools.summary_tool import summary_tool

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools = [search_tool, calculator_tool, summary_tool]

agent = create_react_agent(llm, tools)

def run_agent(goal: str):
    results = []
    inputs = {"messages": [{"role": "user", "content": goal}]}
    
    for chunk in agent.stream(inputs, stream_mode="values"):
        msg = chunk["messages"][-1]
        if hasattr(msg, "content") and msg.content:
            results.append(msg.content)
    
    return results[-1] if results else "No response generated."