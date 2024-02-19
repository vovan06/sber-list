from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.tokens import RefreshToken

from authsystem.models import User


def register(request, serializer_class: Serializer):
    '''Register new user. Get request and serializer class. Retern new user params and access/refresh tokens'''
    data = serializer_class(data=request.data)
    if data.is_valid():
        user = data.save()
        tokens = _get_access_refresh_tokens_for_user(user)
        
        data = data.data
        data['access'] = tokens['access'] 
        data['refresh'] = tokens['refresh']
        return data, status.HTTP_200_OK

    return data.errors, status.HTTP_400_BAD_REQUEST


def authentication(request, serializer_class: Serializer):
    '''Authenticate user by request, email and password. Return response detail with error/successful message and status code. If data is valid, authenticate user user'''
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    telegram_id = request.data.get('telegram_user_id', None)

    if telegram_id:
        try: 
            user = User.objects.get(telegram_user_id=str(telegram_id))

            if user: 
                return _serialize_user(serializer_class, user)
        except:
            return _authentication_by_emain_and_password(request, email, password, serializer_class, telegram_id)
    else:
        return _authentication_by_emain_and_password(request, email, password, serializer_class, telegram_id)

    return {'detail': 'authentication error'}, status.HTTP_400_BAD_REQUEST

def _get_access_refresh_tokens_for_user(user) -> dict:
    '''Get django user object. Return access and refresh tokens'''
    if user is None:
        raise TypeError('This function get user but not None')
        
    tokens = RefreshToken.for_user(user)
    return {
        'refresh': str(tokens),
        'access': str(tokens.access_token),
    }
    
def _authentication_by_emain_and_password(request, email: str, password: str, serializer_class, telegram_id):
    if not email:
        return {'detail': 'no email'}, status.HTTP_400_BAD_REQUEST

    if not password:
        return {'detail': 'no password'}, status.HTTP_400_BAD_REQUEST
   
    user = authenticate(request, email=email, password=password)
    
    if user and not telegram_id:
        return _serialize_user(serializer_class, user)
    elif user and telegram_id:
        print(user, type(user), user.telegram_user_id)
        user.telegram_user_id = telegram_id
        user.save_base()
        print(user.telegram_user_id)
        return _serialize_user(serializer_class, user)

    return {'detail': 'authentication error'}, status.HTTP_400_BAD_REQUEST


def _serialize_user(serializer_class, user):
    serializer = dict(serializer_class(user).data)
    tokens = _get_access_refresh_tokens_for_user(user)
    serializer['access'] = tokens['access'] 
    serializer['refresh'] = tokens['refresh']
    return serializer, status.HTTP_200_OK