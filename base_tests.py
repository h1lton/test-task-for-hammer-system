from verf.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    numbers = ('+79960005599', '+79960004488', '+79960003377')
    users = dict()

    @classmethod
    def create_user(cls, tel):
        user = User.objects.create(tel=tel)
        token_user = Token.objects.create(user=user)
        cls.users[tel] = {
            'obj': user,
            'token': token_user.key
        }

    def switch_user(self, username):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.users[username]['token'])

    @classmethod
    def create_default_stack_users(cls):
        for username in cls.numbers:
            cls.create_user(username)

    @classmethod
    def setUpTestData(cls):
        cls.create_default_stack_users()

    def setUp(self) -> None:
        self.number = self.numbers[0]
        self.switch_user(self.number)
