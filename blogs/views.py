from .models import BlogStories
from .serializers import UserSerializer, BlogStoriesSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.conf import settings
import jwt
import secrets

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogStoriesViewSet(viewsets.ModelViewSet):
    queryset = BlogStories.objects.all()
    serializer_class = BlogStoriesSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            # Generate a new session key if it doesn't exist
            if not request.session.session_key:
                request.session.create()

            session_key = request.session.session_key
            
            # Generate a JWT token containing session key
            payload = {'username': user.username, 'session_key': session_key}
            jwt_secret_key = secrets.token_hex(64)
            jwt_token = jwt.encode(payload, jwt_secret_key, algorithm='HS256')

            # Save or update the token associated with the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'token': jwt_token,
                'user': user.username,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

