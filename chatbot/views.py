from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


class ChatbotView(APIView):
    def post(self, request, *args, **kwargs):
        session_id = request.data.get('session_id')
        message = request.data.get('message')

        # Retrieve or create UserState
        user, created = User.objects.get_or_create(session_id=session_id)

        # Implement your state machine logic here
        # Update user state based on the received message

        # Example: Update state based on a simple condition
        greetings = ["hello", "greetings", "hi", "hey"]
        questions = ["how are you", "howzit", ""]

        if "hello" in message.lower():
            user.current_state = "greeting"
        elif "bye" in message.lower():
            user.current_state = "question"
        else:
            user.current_state = "end"

        user.save()

        # Serialize and return the updated state
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
