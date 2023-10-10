from drf_yasg import openapi
from base_scheme import response_error, tel_schema

ref_code = openapi.Schema(
    type=openapi.TYPE_STRING,
    title='ref_code',
)

profile_schema = {
    'operation_description': 'Профиль пользователя.'
                             '\n\n (Для авторизованных пользователей)',
    'responses': {
        200: openapi.Response(
            '',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'tel': tel_schema,
                    'your_ref_code': ref_code,
                    'used_ref_code': ref_code,
                    'referrals': openapi.Schema(
                        title='referrals',
                        type=openapi.TYPE_ARRAY,
                        items=tel_schema
                    )
                }
            ),
        ),
        401: response_error('Error: Unauthorized')
    }
}

set_referrer_schema = {
    'operation_description': 'Устанавливает реферера по его реферальному коду.'
                             ' (Referrer - человек который пригласил реферала)'
                             '\n\n (Для авторизованных пользователей)',
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'ref_code': openapi.Schema(
                type=openapi.TYPE_STRING,
                example='c8as92'
            )
        },
        required=['code']
    ),
    'responses': {
        204: openapi.Response('Реферер успешно установлен'),
        400: response_error('Error: Bad Request'),
        401: response_error('Error: Unauthorized'),
    }
}
