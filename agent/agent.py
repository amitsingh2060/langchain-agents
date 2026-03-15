from langchain.agents import create_agent
from config.llm import get_llm
from tools.search_tool import get_search_tool
from tools.calculator_tool import calculator
from tools.python_tool import run_python
from tools.date_tool import get_current_date

system_prompt="""
You are an AI assistant that has access to tools.

Rules:
- Use the calculator tool ONLY for valid math expressions.
- If the expression contains invalid characters, respond that it is not a valid math expression.
- Do NOT guess the result of math yourself.
- Use tools when necessary.
"""

def build_agent():

    llm = get_llm()

    tools = [
        get_search_tool(),
        calculator,
        run_python,
        get_current_date
    ]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful AI assistant"
    )

    return agent