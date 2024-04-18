from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user




class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username")
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if username and password:
            # Note: Handle login with username and email logic as per your requirements
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if user and user.email == email:
                data['user'] = user
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username", "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        return data