import jwt

from django.conf import settings
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)

from authsystem.models import User

class JWTAuthClass(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(' ')

        if len(auth_token) != 2:
            #raise AuthenticationFailed('Token not valid')
            return None

        token = auth_token[1]

        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, 'HS256')
            user = User.objects.get(pk=decoded['user_id'])
            return (user, token)

        except:
            return None

        #except jwt.ExpiredSignatureError as ex:
        #    raise AuthenticationFailed('Token not expired')
        #except jwt.DecodeError as ex:
        #    raise AuthenticationFailed('Token is invalid')
        #except User.DoesNotExist as ex:
        #    raise AuthenticationFailed('Invalid data')