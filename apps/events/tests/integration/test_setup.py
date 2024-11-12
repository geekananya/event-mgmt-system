import uuid
from apps.users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.test import APITestCase

class TestEventsSetup(APITestCase):

    fixtures = ['events.json', 'users.json']

    def setUp(self):

        fake_email = f"{str(uuid.uuid4())}@email.com"
        fake_password = 'secret'
        self.user = User.objects.create_user(
            email=fake_email,
            password=fake_password,
            is_admin=True
        )
        self.token = Token.objects.create(user=self.user)

        self.regular_user = User.objects.create_user(
            email='regular@user.com',
            password='regular',
            is_admin=False
        )