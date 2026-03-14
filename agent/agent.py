from langchain.agents import create_agent
from config.llm import get_llm
from tools.search_tool import get_search_tool
from tools.calculator_tool import calculator
from tools.python_tool import run_python


def build_agent():

    llm = get_llm()

    tools = [
        get_search_tool(),
        calculator,
        run_python
    ]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful AI assistant"
    )

    return agent