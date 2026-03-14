from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
# LLM
llm = ChatOllama(model="llama3.1")

# Tool
search = DuckDuckGoSearchRun()

tools = [search]

# Create agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant",
    # debug=True
)

question = "What is the weather in Kanpur today?"
def ask(agent, question):
    return agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
# Run agent
# response = agent.invoke(
#     {"messages": [{"role": "user", "content": question}]}
# )
response = ask(agent, "What is the weather in Kanpur today?")
# Print only the final AI response
print(response["messages"][-1].content)
# print(response)