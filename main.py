# from langchain.agents import create_agent
# from langchain_ollama import ChatOllama
# from langchain_community.tools import DuckDuckGoSearchRun


# llm = ChatOllama(model="llama3.1")

# tools = [DuckDuckGoSearchRun()]

# agent = create_agent(
#     model=llm,
#     tools=tools,
#     system_prompt="You are a helpful assistant"
# )

# chat_history = []

# def ask(question):
#     chat_history.append({
#         "role": "user",
#         "content": question
#     })

#     response = agent.invoke({
#         "messages": chat_history
#     })

#     answer = response["messages"][-1].content

#     chat_history.append({
#         "role": "assistant",
#         "content": answer
#     })

#     return answer


# print(ask("Who is the prime minister of India?"))
# print(ask("What is his age?"))

# from langchain.agents import create_agent
# from langchain_ollama import ChatOllama
# from langchain_community.tools import DuckDuckGoSearchRun


# # LLM
# llm = ChatOllama(model="llama3.1")

# # Tools
# tools = [DuckDuckGoSearchRun()]

# # Agent
# agent = create_agent(
#     model=llm,
#     tools=tools,
#     system_prompt="You are a helpful assistant"
# )

# # Memory
# chat_history = []


# def ask(question):
#     global chat_history

#     # add user message
#     chat_history.append({
#         "role": "user",
#         "content": question
#     })

#     # send conversation to agent
#     response = agent.invoke({
#         "messages": chat_history
#     })

#     # get AI answer
#     answer = response["messages"][-1].content

#     # store AI answer
#     chat_history.append({
#         "role": "assistant",
#         "content": answer
#     })

#     return answer


# # Interactive chatbot loop
# while True:
#     question = input("You: ")

#     # exit condition
#     if question.lower() in ["exit", "quit", "bye"]:
#         print("AI: Goodbye 👋")
#         break

#     answer = ask(question)
#     print("AI:", answer)

from agent.agent import build_agent
from memory.chat_memory import add_user_message, add_ai_message, get_history

agent = build_agent()

def ask(question):

    add_user_message(question)

    response = agent.invoke({
        "messages": get_history()
    })

    answer = response["messages"][-1].content

    add_ai_message(answer)

    return answer


while True:

    # question = input("You: ")
    question = "What is LangChain?"
    if question.lower() in ["exit", "quit"]:
        print("AI: Goodbye 👋")
        break

    print("AI:", ask(question))