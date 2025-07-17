import datetime
import random
def Sky(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "chatgpt" in user_input or "chat gpt" in user_input:
        return "i know about it.It is also a chat bot with large llms."
    elif "help" in user_input:
        return "I can assist you with general queries like time, greetings, or saying goodbye."
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm Sky, your friendly chatbot!"
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."
    elif "day" in user_input or "month" in user_input:
        now = datetime.datetime.now()
        return f"Today is {now.day} {now.strftime('%B')}."
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"

print("Chatbot: Hello! Type something to chat or 'exit' to stop.")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        goodbyes = ["Bye!", "See you later!", "Goodbye!" ,"waiting for you again!"]
        print("Chatbot:", random.choice(goodbyes))
        break
    Skyresponse = Sky(user)
    print("Chatbot:", Skyresponse)