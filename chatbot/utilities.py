def get_greeting_response(input: str) -> str:

    if input == "hello":
        return "Hello there!"
    elif input == "greetings":
        return "greetings"
    elif input == "hi":
        return "Hi there, buddy!"
    elif input == "hey":
        return "Hi there, buddy!"


def get_question_response(input: str) -> str:

    if input == "how are you":
        return "I am good thanks"
    elif input == "howzit":
        return "I'm all good"
    elif input == "how you doing":
        return "I'm ok thanks, buddy!"
    elif input == "what is your name":
        return "My name is Botty, thanks for asking"
    elif input == "how old are you":
        return "I am just a few days old"


def get_ending_response(input: str) -> str:

    if input == "bye":
        return "See you, then"
    elif input == "see you":
        return "Was nice chatting to you"
    elif input == "got to go":
        return "See you soon"
