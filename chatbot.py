def chatbot_response(state, action, when):

    if state == "overwhelmed":
        return f"You seem overwhelmed. Let’s slow down—try {action} {when}."

    elif state == "restless":
        return f"You seem restless. Try {action} {when} to feel better."

    elif state == "focused":
        return f"You’re in a good state. This is a great time for {action} {when}."

    elif state == "calm":
        return f"You seem calm. You can continue with {action} {when}."

    elif state == "mixed":
        return f"You have mixed feelings. Try {action} {when} to gain clarity."

    elif state == "neutral":
        return f"You seem neutral. {action} {when} could help you move forward."

    return f"Try {action} {when} to improve your current state."