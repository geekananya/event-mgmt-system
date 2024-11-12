from django.urls import reverse
from rest_framework import status
from apps.users.tests.integration.test_setup import TestUsersSetup

class TestAuthAPI(TestUsersSetup):

    def test_get_all_users(self):

        url = reverse('getusers')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)


    def test_get_user_by_id(self):
        url = reverse('getuser', kwargs={'pk':3})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('email'), 'dummy@user.com')


    def test_delete_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('deleteuser', kwargs={'pk': 2})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_not_authorized(self):
        url = reverse('deleteuser', kwargs={'pk': 13})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)