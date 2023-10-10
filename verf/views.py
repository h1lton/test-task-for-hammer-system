from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .permissions import IsUnauthenticated
from .scheme import send_code_schema, check_code_schema
from .utils import VerfCode, serialize_tel


class SendCodeView(APIView):
    permission_classes = [IsUnauthenticated]

    @swagger_auto_schema(**send_code_schema)
    def post(self, request, *args, **kwargs):
        tel = serialize_tel(request.data.get('tel'))
        VerfCode(tel).send()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckCodeView(APIView):
    permission_classes = [IsUnauthenticated]

    @swagger_auto_schema(**check_code_schema)
    def post(self, request, *args, **kwargs):
        tel = serialize_tel(request.data.get('tel'))
        code = request.data.get('code')

        VerfCode(tel, code=code).is_valid()

        user = User.objects.get_or_create(tel=tel)[0]
        token = Token.objects.get_or_create(user=user)[0]
        data = {'auth_token': token.key}
        return Response(status=status.HTTP_200_OK, data=data)
