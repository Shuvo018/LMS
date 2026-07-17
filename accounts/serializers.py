from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers  import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'password1', 'password2')


    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise ValueError({'password': 'Password does not match!'})
        
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        return User.objects.create_user(password=password, **validated_data)
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)
        token['email'] = user.email
        token['role'] = user.role

        return token
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPassword(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField(min_length=8)
