from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from authentication.views import SignUpView


class TestsSignUpView(TestCase):
    def _request(self):
        request = self.factory.post('/api/sign-up/', self.request_data)
        sign_up_view = SignUpView.as_view()
        response = sign_up_view(request)
        return response

    def setUp(self):
        self.factory = APIRequestFactory()
        self.request_data = {
            'username': 'maria',
            'email': 'maria.silva@teste.com',
            'first_name': 'Maria',
            'last_name': 'Silva',
            'password_1': 'a@9cJ3b%',
            'password_2': 'a@9cJ3b%'
        }

    def test_create_new_user(self):
        response = self._request()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_created_passwords_not_identical(self):
        self.request_data['password_2'] = 'a@9cJ3b*'
        response = self._request()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
