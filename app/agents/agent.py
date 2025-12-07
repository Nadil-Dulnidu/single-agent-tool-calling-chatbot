from app.agents.prompts import system_prompt
from app.core import llm
from app.agents.tools import add, subtract, multiply, exponentiate, serpapi
from langchain.agents import create_agent

# Tool mapping
tools = [add, subtract, multiply, exponentiate, serpapi]

agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    tools=tools,
)

# if __name__ == "__main__":
#     import asyncio
#     from langchain_core.messages import HumanMessage
    
#     async def main():
#         response = await agent.ainvoke({"messages": [HumanMessage(content="what is 2 to the power of 8?")]})
#         print("Agent response:", response["messages"][-1])

#     asyncio.run(main())