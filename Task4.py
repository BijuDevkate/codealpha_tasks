def get_response(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hi!"
    elif "how are you" in msg:
        return "I am fine, thanks for asking"
    elif "your name" in msg:
        return "I am a simple chatbot"
    elif "who made you" in msg:
        return "I was created using Python"
    elif "bye" in msg or "exit" in msg:
        return "Goodbye!"
    elif "help" in msg:
        return "You can ask about greetings, time, or me"
    elif "time" in msg:
        from datetime import datetime
        return "Current time is " + datetime.now().strftime("%H:%M:%S")
    elif "date" in msg:
        from datetime import datetime
        return "Today is " + datetime.now().strftime("%Y-%m-%d")
    elif "thank" in msg:
        return "You're welcome"
    elif "weather" in msg:
        return "I can't access live weather, but I hope it's nice"
    elif "joke" in msg:
        return "Why did the computer get cold? Because it forgot to close its Windows"
    else:
        return "I don't understand that"

print("Chatbot started. Type bye to exit.")

while True:
    user = input("You: ")
    reply = get_response(user)
    print("Bot:", reply)
    if "bye" in user.lower() or "exit" in user.lower():
        break
