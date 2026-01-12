from openai import OpenAI
from dotenv import load_dotenv
import os
"""
this is the program to get the data of .env file
"""
from langchain.agents import create_agent

load_dotenv()   # 🔑 Loads .env file
print(os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
