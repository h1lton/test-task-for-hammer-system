from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from verf.models import User
from .scheme import set_referrer_schema, profile_schema
from .serializers import profile_serializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**profile_schema)
    def get(self, request, *args, **kwargs):
        data = profile_serializer(request.user)
        return Response(data=data, status=status.HTTP_200_OK)


class SetReferrerView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**set_referrer_schema)
    def post(self, request, *args, **kwargs):
        user = request.user
        ref_code = request.data.get('ref_code')

        if ref_code is None:
            raise ValidationError({'ref_code': 'This field is required.'})
        elif user.referrer_id is not None:
            raise ValidationError({'ref_code': 'You already have a referrer.'})
        elif user.ref_code == ref_code:
            raise ValidationError({'ref_code': 'You cannot use your own referral code.'})

        try:
            user.referrer = User.objects.get(ref_code=ref_code)
        except User.DoesNotExist:
            raise ValidationError({'ref_code': 'This referral code does not exist.'})

        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
