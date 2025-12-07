from langgraph.graph import StateGraph, MessagesState, START
from app.agents import agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

async def agent_node(state: MessagesState):
    messages = state["messages"]
    response = await agent.ainvoke({"messages": messages},)
    return {"messages": response["messages"][-1]}
    
workflow = StateGraph(MessagesState)
workflow.add_node("agent", agent_node)
workflow.add_edge(START, "agent")
app_graph = workflow.compile(checkpointer=checkpointer)
    