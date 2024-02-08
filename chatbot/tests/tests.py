from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from chatbot.models import User, Step


class ChatBotTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(session_name="name", current_state="greeting")
        self.step = Step.objects.create(state_name="greeting", response_message="Hello")

    def test_chat_endpoint(self):
        url = '/chat/'

        # Test with a valid input
        data = {"session_name": self.user.session_id, "input": "Hello"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Hello", response.data["message"])

        # Test with an invalid session_id
        data = {"session_name": "invalid_session", "input": "Hello"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Add more test cases as needed

    def test_state_machine_logic(self):
        # Test the state transition logic

        # For example, assuming a transition from greeting to question
        self.user.current_state = "greeting"
        self.user.save()

        data = {"session_name": self.user.session_id, "input": "What services do you offer?"}
        response = self.client.post('/chat/', data, format='json')

        # Assuming state transition logic is implemented in the view
        updated_user = User.objects.get(session_name=self.user.session_name)
        self.assertEqual(updated_user.current_state, "question")
