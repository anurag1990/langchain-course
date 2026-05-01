from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from langchain_tavily import TavilySearch

tavily_client = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    response = tavily_client.search(query)
    return response

llm = ChatOpenAI(model="gpt-5")
tools = [search]
"""
Or tavily search tool
tools=[TavilySearch()]
"""
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result= agent.invoke({"messages":HumanMessage(content="What's the weather in Bangalore?")})
    print(result)

if __name__ == "__main__":
    main()
