import uuid
from apps.users.models import User
from django.http import Http404
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.test import APITestCase

class TestUsersSetup(APITestCase):

    fixtures = ['users.json']

    def setUp(self):

        fake_email = f"{str(uuid.uuid4())}@email.com"
        fake_password = 'secret'
        self.user = User.objects.create_user(
            email=fake_email,
            password=fake_password,
            is_admin=True,
            is_staff=True
        )
        self.token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION=f'Token {str(token.key)}')
        # self.my_model = MyModel.objects.create(
        #     field1 = some_value,
        #     field2 = some_value,
        #     user = self.user
        # )