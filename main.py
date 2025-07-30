from fastapi import FastAPI
from pydantic import BaseModel
from agent.fitness_agent import fitness_agent
from agents import Runner
from fastapi.middleware.cors import CORSMiddleware
from datatypes.datatype import ChatRequestBody, ChatResponse,ChatInput


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
async def chat(request: ChatInput):
    # user_question = request.message
    user_data = request.input
    # todays_workout = request.todaysWorkout
    
#     template_input = f"""
#  Here is the user's fitness profile:
# - Fitness Goal: {user_data['fitnessGoal']}
# - Fitness Level: {user_data['fitnessLevel']}
# - Age: {user_data['age']}
# - Gender: {user_data['gender']}
# - Height: {user_data['height']}
# - Weight: {user_data['weight']}
# - Equipment Available: {', '.join(user_data['equipment'])}
# - Workout Days Per Week: {user_data['workoutDaysPerWeek']}
# - Injuries: {', '.join(user_data['injuries']) if user_data['injuries'] else 'None'}
# - Diet Preference: {user_data['dietPreference']}

# Today's workout plan:
# - Title: {todays_workout['title']}
# - Duration: {todays_workout['duration']}
# - Exercises:
# {chr(10).join([f"  • {ex['name']} ({ex['duration']}, {ex['type']}): {ex['instructions']}" for ex in todays_workout['exercises']])}

# User's question:
# {user_question}

# Please answer as a helpful, motivating fitness coach. If relevant, use the user's profile and today's workout plan in your response.
# """
    
    resp = await Runner.run(fitness_agent, input=user_data)
    

    agent_output = resp.final_output
    

    return ChatResponse(output=agent_output)

