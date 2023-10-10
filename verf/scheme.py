from drf_yasg import openapi
from base_scheme import response_error, tel_schema

send_code_schema = {
    'operation_description': 'Отправляет код верификации по смс на переданный номер телефона.'
                             '\n\n (Для НЕ авторизованных пользователей)',
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'tel': tel_schema
        },
        required=['tel']
    ),
    'responses': {
        204: openapi.Response('Код успешно отправлен на указанный номер телефона.'),
        400: response_error('Error: Bad Request')
    }
}

check_code_schema = {
    'operation_description': 'Проверяет введённый код верификации, если он верный возвращает токен авторизации.'
                             '\n\n (Для НЕ авторизованных пользователей)',
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'tel': tel_schema,
            'code': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='9102',
                description='Код верификации который был получен с помощью /verf/send_code/'
            )
        },
        required=['tel', 'code']
    ),
    'responses': {
        200: openapi.Response(
            '',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'auth_token': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example='2b2ea1f18dea1esa5c5s7cba133c99c1b8cc2zf',
                        description='Токен авторизации'
                    )
                }
            )
        ),
        400: response_error('Error: Bad Request')
    }
}
