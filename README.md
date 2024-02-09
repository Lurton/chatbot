# chatbot

# TO RUN THE PROGRAM DO THE FOLLOWING:
# make sure you've got python installed

# 1) if pipenv is not installed run the command: pip install pipenv

# 2) after cloning the chatbot project from github cd into the project's root directory and run this command:
#   pipenv sync

# 3) then run: pipenv run python manage.py migrate

# 4) then run: pipenv run python manage.py runserver

# 5) Hit the url http://localhost:8000/api/chatbot/

# 6) Post a dictionary containin a session_name and message in the content field and you will receive a json response
# containing your input and the appropriate response. eg. {"session_name": "name","message": "hello"}  Allowed inputs include:

# greetings = ["hello", "greetings", "hi", "hey"] for greetings
# questions = ["how are you", "howzit", "how you doing", "what is your name", "how old are you", ] for questions
# endings = ["bye", "see you", "got to go"] for ending the convo

# Please note that I tried posting using curl but it was not working on my cmd, not sure what's changed with it.

# To run tests run the following command: pipenv run coverage run manage.py test -v 2