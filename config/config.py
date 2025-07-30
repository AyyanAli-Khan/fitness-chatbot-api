from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
from decouple import config

api_key = config('GEMINI_API_KEY')
base_url = config('BASE_URL')
model = config("MODEL")



client = AsyncOpenAI(api_key=api_key, base_url=base_url)

model = OpenAIChatCompletionsModel(model=model,openai_client=client)

