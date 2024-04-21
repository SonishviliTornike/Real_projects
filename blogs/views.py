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
            token, created = Token.objects.get_or_create(user=user)
            session_key = request.session.session_key
            return Response({
            'session_key': session_key,
            'user': user.username
            }, status=status.HTTP_200_OK)
            
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)






























