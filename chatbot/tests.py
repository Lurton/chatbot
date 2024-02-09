from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from chatbot.models import User, Log


class ChatBotTests(TestCase):
    """
    This test case is used to test all the chatbot's api endpoint and functions.
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(session_name="name", current_state="greeting")

    def test_chatbot_endpoint(self):
        url = reverse("chatbot")

        # Test with a valid greeting input
        data = {"session_name": self.user.session_name, "message": "hello"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        reply = Log.objects.all().last()
        self.assertEqual(reply.response, "Hello there!")


        data = {"session_name": self.user.session_name, "message": "Invalid input"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

