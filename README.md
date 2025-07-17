# -CODSOFT_1
---
title: "Sky Chatbot: A Professional Conversational Interface"
author: "Javaji GaganSai"
date: "2025-07-17"
---
# Sky Chatbot Implementation

## Overview

This R Markdown document presents the implementation of Sky, a professional conversational chatbot designed to handle basic user queries with a focus on reliability and user-friendly interaction. The chatbot is implemented in Python and integrated into this R Markdown file using the `reticulate` package for seamless execution within an R environment.

## Purpose

The Sky Chatbot serves as a lightweight conversational interface capable of responding to common queries, including greetings, time and date requests, and farewells. It is designed for extensibility and can be adapted for various professional applications, such as customer support or informational services.

Ensure a Python environment with the `datetime` and `random` modules is accessible.

## Implementation

### Python Code

The following Python code defines the `Sky` function and the main interaction loop:

```{python}
import datetime
import random

def Sky(user_input):
    """
    Process user input and return an appropriate response.
    
    Args:
        user_input (str): The user's input string.
        
    Returns:
        str: A response based on the input.
    """
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Greetings! How may I assist you today?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Thank you for using Sky. Goodbye."
    elif "chatgpt" in user_input or "chat gpt" in user_input:
        return "ChatGPT is another conversational AI model. I am Sky, designed for efficient and targeted responses."
    elif "help" in user_input:
        return "I can assist with queries related to time, date, greetings, or general information. Please specify your request."
    elif "your name" in user_input or "who are you" in user_input:
        return "I am Sky, a professional chatbot created by xAI."
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"The current date is {current_date}."
    elif "day" in user_input or "month" in user_input:
        now = datetime.datetime.now()
        return f"Today is {now.strftime('%A')}, {now.day} {now.strftime('%B')}."
    else:
        return "I apologize, but I am unable to process that request. Please try a different query."

def main():
    """
    Main function to run the Sky Chatbot interactively.
    """
    print("Sky Chatbot: Welcome! Type your query or 'exit' to terminate the session.")
    while True:
        user = input("User: ")
        if user.lower() == "exit":
            goodbyes = ["Thank you for your session. Goodbye.", 
                       "Session terminated. Have a great day!", 
                       "Thank you for using Sky. Farewell."]
            print("Sky Chatbot:", random.choice(goodbyes))
            break
        response = Sky(user)
        print("Sky Chatbot:", response)

if __name__ == "__main__":
    main()
```

## Execution Instructions

The Python code above is designed for interactive execution in a Python environment (e.g., Python console, Jupyter Notebook, or terminal). Due to the interactive nature of the `input()` function, it may not run directly when knitting this R Markdown document. To test the chatbot:

1. Copy the Python code into a Python environment.
2. Run the script to initiate the chatbot.
3. Interact by typing queries or "exit" to end the session.

Alternatively, the code can be adapted for R environments using `reticulate` with a custom input mechanism, though this requires additional configuration.

## Functionality

The Sky Chatbot processes user input with the following capabilities:

- **Greetings**: Responds to "hello" or "hi" with a professional welcome.
- **Farewells**: Handles "bye" or "goodbye" with courteous exit messages.
- **Identity Queries**: Responds to "your name" or "who are you" with a clear introduction.
- **Time/Date Queries**: Provides the current time, date, or day/month using the `datetime` module.
- **Help Requests**: Offers guidance on supported queries.
- **ChatGPT Mentions**: Acknowledges ChatGPT while highlighting Sky's unique design.
- **Default Response**: Politely handles unrecognized inputs.

Randomized farewell messages enhance the user experience by adding variety to session terminations.

## Example Interaction

Below is a sample interaction when running the chatbot in a Python environment:

```
Sky Chatbot: Welcome! Type your query or 'exit' to terminate the session.
User: Hello
Sky Chatbot: Greetings! How may I assist you today?
User: What is the time?
Sky Chatbot: The current time is 12:35:00.
User: Who are you?
Sky Chatbot: I am Sky, a professional chatbot created by xAI.
User: exit
Sky Chatbot: Thank you for your session. Goodbye.
```

## Deployment Considerations

For professional deployment, consider the following enhancements:

- **Web Interface**: Integrate the chatbot with a web framework (e.g., Flask or Django) for broader accessibility.
- **Extended Functionality**: Add support for more complex queries or integration with external APIs.
- **R Integration**: Use `reticulate` to create an interactive R Shiny application for running the chatbot within R environments.
- **Logging**: Implement logging to track user interactions for analytics and improvements.

## Conclusion

The Sky Chatbot is a robust and extensible solution for basic conversational tasks. Its modular design allows for easy integration into professional workflows, making it suitable for customer-facing applications or internal tools.
