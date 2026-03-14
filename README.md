ollama run llama3
#ollama serve

langchain-agent/
│
├── main.py                # Entry point (chat loop)
│
├── agent/
│   └── agent.py           # Agent creation logic
│
├── tools/
│   ├── search_tool.py     # DuckDuckGo search tool
│   ├── calculator_tool.py # Math calculator tool
│   └── python_tool.py     # Python execution tool
│
├── memory/
│   └── chat_memory.py     # Chat history logic
│
├── config/
│   └── llm.py             # LLM configuration
│
└── requirements.txt

In LangGraph:
User Input
     ↓
LLM Node
     ↓
Tool Node
     ↓
LLM Node
     ↓
Final Answer

Node → a function that runs

Edge → connection between nodes

State → shared data between nodes