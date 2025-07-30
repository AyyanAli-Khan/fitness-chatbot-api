from fastapi import FastAPI
from pydantic import BaseModel
from agent.fitness_agent import fitness_agent
from agents import Runner
from datatypes.datatype import ChatRequest, ChatResponse


app = FastAPI()

@app.get("/")
def home():
    return {'API is': "working"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_input = request.input
    
    resp = await Runner.run(fitness_agent, input=user_input)
    

    agent_output = resp.final_output
    

    return ChatResponse(output=agent_output)

