from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

User = get_user_model()

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        print(request.headers)

        if not auth_header: 
            return None
        
        if not auth_header.startswith('Bearer'):
            raise PermissionDenied(detail='Invalid token format')
        
        token = auth_header.replace('Bearer ', '')

        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))

        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail='Invalid token')
        
        except User.DoesNotExist:
            raise PermissionDenied(detail='User not found')
        
        return (user, token)
