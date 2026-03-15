from langchain.tools import tool
import re

@tool
def calculator(expression: str) -> str:
    """Evaluate math expressions."""

    if not re.match(r"^[0-9\+\-\*\/\(\)\.\s]+$", expression):
        return "Invalid math expression."

    return str(eval(expression))
