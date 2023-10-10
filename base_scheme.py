from drf_yasg import openapi

tel_schema = openapi.Schema(
    title='tel',
    type=openapi.TYPE_STRING,
    example='+79998887766',
)


def response_error(error, key='detail'):
    return openapi.Response(
        error,
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                key: openapi.Schema(
                    type=openapi.TYPE_STRING,
                    title='detail'
                )
            }
        )
    )
