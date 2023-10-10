from random import choice
from string import digits

from django.core.cache import cache
from rest_framework.exceptions import ValidationError

from .serializers import PhoneNumberSerializer


class VerfCode:
    def __init__(self, tel, code=None):
        self.tel = tel
        self.key = f'vc{tel}'
        self.code = code

    def create(self):
        code = ''.join(choice(digits) for _ in range(4))
        cache.set(self.key, code, 900)
        return code

    def get(self):
        return cache.get(self.key)

    def delete(self):
        return cache.delete(self.key)

    def send(self):
        code = self.create()
        print(self.tel, code)

    def is_valid(self):
        expected_code = self.get()
        if self.code is None:
            raise ValidationError({'ref_code': 'This field is required.'})
        elif expected_code is None:
            raise ValidationError({'code': 'The verification code has expired or you did not request it.'})
        elif expected_code != self.code:
            raise ValidationError({'code': 'Invalid verification code.'})
        else:
            self.delete()


def serialize_tel(tel):
    serializer = PhoneNumberSerializer(data={'tel': tel})
    serializer.is_valid(raise_exception=True)
    tel = str(serializer.validated_data['tel'])
    return tel
