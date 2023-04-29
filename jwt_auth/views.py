from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, NotFound
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView


from .serializers.common import UserSerializer
from .serializers.populated import PopulatedUserSerializer

User = get_user_model()


class RegisterView(APIView):

    def post(self, request):
        print(request.data)
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_202_ACCEPTED)
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try: 
            user_to_login = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied(detail="No user found with that email. Please register as a new user.")
        
        if not user_to_login.check_password(password):
            raise PermissionDenied(detail="Invalid Credentials")
        
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode(
            {'sub': user_to_login.id, 'exp': int(dt.strftime('%s'))},
            settings.SECRET_KEY, 
            algorithm='HS256'
        )

        return Response({'token': token, 'message': f"Welcome back {user_to_login.username}"})
    
class UserListView(APIView):
    def get(self, _request):
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_202_ACCEPTED)

class UserDetailView(APIView):
    
    def get_user(self, pk):
        try: 
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(detail="No user with that id can be found.")
        
    def get(self, _request, pk):
        user = self.get_user(pk=pk)
        serialized_user = PopulatedUserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
    


    # Update user details
    # def put(self, request, pk):
    #     print('You made it the edit endpoint.')
    #     user_to_update = self.get_user(pk=pk); 
    #     user_to_update.bio = request.data.get('bio', user_to_update.bio)
    #     updated_user = UserSerializer(user_to_update, exclude=['passpord', 'password_confirmation', 'username', 'email'])
    #     print(request.data)
    #     try:
    #         print(updated_user)
    #         updated_user.is_valid()
    #         print(updated_user.is_valid())
    #         print(updated_user.errors)
    #         updated_user.save()
    #         return Response(updated_user.data, status=status.HTTP_202_ACCEPTED)
    #     except AssertionError as e:
    #         return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #     except: 
    #         return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
  
