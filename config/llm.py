# from langchain_ollama import ChatOllama

# def get_llm():
#     return ChatOllama(model="llama3.1")

# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# from langchain_openai import ChatOpenAI


# def get_llm():
#     return ChatOpenAI(
#         model="gpt-4o-mini",
#         temperature=0,
#         api_key=os.getenv("OPENAI_API_KEY")  # optional but safer
#     )


from dotenv import load_dotenv
import os

load_dotenv()

from langchain_groq import ChatGroq


def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",   # fast + free
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )