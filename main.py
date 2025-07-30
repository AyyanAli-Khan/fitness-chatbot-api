from fastapi import FastAPI
from pydantic import BaseModel
from agent.fitness_agent import fitness_agent
from agents import Runner
from fastapi.middleware.cors import CORSMiddleware
from datatypes.datatype import ChatRequest, ChatResponse


app = FastAPI()



# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def home():
    return {'API is': "working"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_input = request.input
    
    resp = await Runner.run(fitness_agent, input=user_input)
    

    agent_output = resp.final_output
    

    return ChatResponse(output=agent_output)

