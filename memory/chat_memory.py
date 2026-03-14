chat_history = []

def add_user_message(msg):
    chat_history.append({"role": "user", "content": msg})

def add_ai_message(msg):
    chat_history.append({"role": "assistant", "content": msg})

def get_history():
    return chat_history