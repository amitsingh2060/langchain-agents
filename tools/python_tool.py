from langchain.tools import tool

@tool
def run_python(code: str) -> str:
    """Execute python code."""
    local_vars = {}
    exec(code, {}, local_vars)
    return str(local_vars)