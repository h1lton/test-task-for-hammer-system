from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .utils import VerfCode


class VerfTests(APITestCase):
    def post_send(self, data):
        return self.client.post(reverse('send-code'), data=data)

    def post_check(self, data):
        return self.client.post(reverse('check-code'), data=data)

    def test_valid_login(self):
        tel = '+79112223344'

        data = {'tel': tel}
        response = self.post_send(data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        data['code'] = VerfCode(tel).get()
        response = self.post_check(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_token = Token.objects.get(user__tel='+79112223344').key
        response_token = response.data['auth_token']
        self.assertEqual(expected_token, response_token)

    def test_invalid_country_code_in_number(self):
        data = {'tel': '911223344'}
        response = self.post_send(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_code_validations(self):
        tel = '+79112223344'
        data = {'tel': tel}
        response = self.post_check(data)
        self.assertEqual(response.data, {'ref_code': 'This field is required.'})

        data['code'] = '0000'
        response = self.post_check(data)
        self.assertEqual(response.data, {'code': 'The verification code has expired or you did not request it.'})

        self.post_send(data)
        response = self.post_check(data)
        self.assertEqual(response.data, {'code': 'Invalid verification code.'})

        data['code'] = VerfCode(tel).get()
        response = self.post_check(data)
        self.assertEqual(list(response.data.keys()), ['auth_token'])
