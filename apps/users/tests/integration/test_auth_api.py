from django.urls import reverse
from rest_framework import status
from apps.users.tests.integration.test_setup import TestUsersSetup
from apps.users.models import User

class TestAuthAPI(TestUsersSetup):

    def test_login(self):
        url = reverse('login')
        data = {
            'email': 'admin@gmail.com',
            'password': 'admin',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsNot(response.data.get('token'), "" or None)


    def test_register(self):

        url = reverse('registeruser')
        data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@user.com',
            'password': 'test',
            'is_admin': False
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email=data['email'])
        self.assertEqual(str(user), 'test@user.com')
        self.assertTrue(user.check_password('test'))

        self.assertIsNot(response.data.get('token'), "" or None)


    def test_logout_invalid_token(self):
        url = reverse('logout')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token r-a-n-d-o-m-0-token-%83')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)