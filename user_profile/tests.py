from django.urls import reverse
from rest_framework import status

from base_tests import BaseTestCase
from verf.models import User


class ProfileTests(BaseTestCase):
    def post_set_referrer(self, data=None):
        return self.client.post(reverse('set-referrer'), data=data)

    def get_user_profile(self):
        return self.client.get(reverse('user-profile'))

    def test_profile_fields(self):
        response = self.get_user_profile()
        self.assertEqual(tuple(response.data.keys()), ('tel', 'your_ref_code', 'used_ref_code', 'referrals'))

    def test_profile_and_set_referrer(self):
        for number in self.numbers[:-1]:
            self.switch_user(number)
            response = self.get_user_profile()
            self.assertEqual(response.data['used_ref_code'], None)

            ref_code = self.users[self.numbers[-1]]['obj'].ref_code
            data = {'ref_code': ref_code}
            response = self.post_set_referrer(data=data)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = self.get_user_profile()
            self.assertEqual(response.data['used_ref_code'], ref_code)

        self.switch_user(self.numbers[2])
        response = self.get_user_profile()
        self.assertEqual(response.data['referrals'], list(self.numbers[:-1]))

    def test_set_referrer(self):
        ref_code = self.users[self.numbers[1]]['obj'].ref_code
        data = {'ref_code': ref_code}
        response = self.post_set_referrer(data=data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        obj = User.objects.select_related('referrer').only('referrer__ref_code').get(tel=self.number)
        self.assertEqual(obj.referrer.ref_code, ref_code)
        self.assertEqual(list(obj.referrer.referrals.only('tel').values_list('tel', flat=True)), [self.number])

    def test_change_referrer(self):
        ref_code = self.users[self.numbers[1]]['obj'].ref_code
        data = {'ref_code': ref_code}
        self.post_set_referrer(data=data)

        ref_code = self.users[self.numbers[2]]['obj'].ref_code
        data = {'ref_code': ref_code}
        response = self.post_set_referrer(data=data)
        self.assertEqual(response.data, {'ref_code': 'You already have a referrer.'})

    def test_set_referrer_as_yourself(self):
        data = {'ref_code': self.users[self.number]['obj'].ref_code}
        response = self.post_set_referrer(data=data)
        self.assertEqual(response.data, {'ref_code': 'You cannot use your own referral code.'})

    def test_set_referrer_as_none(self):
        response = self.post_set_referrer()
        self.assertEqual(response.data, {'ref_code': 'This field is required.'})

    def test_set_referrer_not_exists(self):
        data = {'ref_code': 'mxvc'}
        response = self.post_set_referrer(data=data)
        self.assertEqual(response.data, {'ref_code': 'This referral code does not exist.'})
