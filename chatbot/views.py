
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Log
from .serializers import UserSerializer, LogSerializer
from .utilities import get_ending_response, get_greeting_response, get_question_response


class ChatbotView(APIView):
    def post(self, request, *args, **kwargs):
        session_name = request.data.get('session_name')
        input = request.data.get('message').lower()

        user, created = User.objects.get_or_create(session_name=session_name)

        greetings = ["hello", "greetings", "hi", "hey"]
        questions = ["how are you", "howzit", "how you doing", "what is your name", "how old are you", ]
        endings = ["bye", "see you", "got to go"]

        if input in greetings:
            user.current_state = "greeting"
            response = get_greeting_response(input)
        elif input in questions:
            user.current_state = "question"
            response = get_question_response(input)
        elif input in endings:
            user.current_state = "end"
            response = get_ending_response(input)
        else:
            response = "Incorrect input. Please try something else"
            data = {"input": input, "response": response}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        user.save()

        log = Log.objects.create(user=user, input=input, response=response)
        log_serialized = {"input": log.input, "response": log.response}

        serializer = LogSerializer(log)
        return Response(serializer.data, status=status.HTTP_200_OK)
