from agno.agent import Agent
from agno.models.openai import OpenAIChat
# from agno.models.groq import Groq
from agno. tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv

load_dotenv ()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["GROQ_API_KEY"]= os. getenv("GROQ")


agent=Agent(
        model=OpenAIChat("gpt-3.5-turbo"),
        description="You are an assistant please reply based on the question",
        tools=[DuckDuckGoTools()],
        markdown =True
         )

agent.print_response("who won ipl match on 8.4.2025 ,with score")