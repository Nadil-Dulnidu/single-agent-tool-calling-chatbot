from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from app.agents import app_graph
from langchain_core.messages import HumanMessage

# initilizing our application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

config = {"configurable": {"thread_id": "thread-1"}}

async def response_generator(user_query: str):
    initial_state = {"messages": [HumanMessage(content=user_query)]}
    # astream_events (v2) exposes the internal events of the LLM
    async for event in app_graph.astream_events(initial_state, version="v2", config=config):
        # We only care about the LLM actually generating text tokens
        if event["event"] == "on_chat_model_stream":
            # Get the token (chunk)
            chunk = event["data"]["chunk"]
            # Filter out tool calls or empty chunks, yield only text content
            if chunk.content:
                yield chunk.content
                
# invoke function
@app.post("/invoke")
async def invoke(content: str):
    # return the streaming response
    return StreamingResponse(
        response_generator(content),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )


# chat function