from pydantic import BaseModel
from typing import List




class Exercise(BaseModel):
    name: str
    duration: str
    type: str
    instructions: str

class TodaysWorkout(BaseModel):
    title: str
    duration: str
    exercises: List[Exercise]

class UserData(BaseModel):
    fitnessGoal: str
    fitnessLevel: str
    age: int
    gender: str
    height: float
    weight: float
    equipment: List[str]
    workoutDaysPerWeek: int
    injuries: List[str]
    dietPreference: str

class ChatRequestBody(BaseModel):
    message: str
    userData: UserData
    todaysWorkout: TodaysWorkout

    
    
class ChatResponse(BaseModel):
    output: str
    
    