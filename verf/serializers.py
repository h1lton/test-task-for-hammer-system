from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import User


class PhoneNumberSerializer(serializers.Serializer):
    tel = PhoneNumberField()
