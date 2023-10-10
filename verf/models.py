from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def generate_ref():
    return uuid4().hex[:6]


class User(models.Model):
    tel = PhoneNumberField(unique=True)
    ref_code = models.CharField(max_length=6, default=generate_ref, unique=True)
    referrer = models.ForeignKey('self',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='referrals',
                                 )

    USERNAME_FIELD = 'tel'
    REQUIRED_FIELDS = []
    is_active = True
    is_anonymous = False
    is_authenticated = True
