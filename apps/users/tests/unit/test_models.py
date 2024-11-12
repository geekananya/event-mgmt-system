from rest_framework.test import APITestCase
from apps.users.models import User

class TestUserModel(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            first_name = 'user21',
            email ='user@gamidl.com',
            password='test',
            is_admin =  True,
        )
        self.user2 = User.objects.create_superuser(
            first_name = 'user22',
            password='testsuper',
            email ='super@user.com',
        )


    def test_user_str(self):
        self.assertEqual(str(self.user1), 'user@gamidl.com')
        self.assertEqual(str(self.user2), 'super@user.com')

    def test_hashed_password(self):
        self.assertIsNot(self.user1.password, 'test')
        self.assertIsNot(self.user2.password, 'testsuper')
