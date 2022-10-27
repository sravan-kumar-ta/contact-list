from django.contrib.auth.models import User
from rest_framework import serializers

from authentication.models import Contact


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# class LoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['email', 'password', 'username', 'get_full_name', 'role', 'tokens']
#         read_only_fields = ['username', 'role']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         password = attrs.get('password', '')
#         filtered_user_by_email = CustomUser.objects.filter(email=email)
#         user = CustomAuth.authenticate(username=email, password=password)
#
#         if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
#             raise AuthenticationFailed(
#                 detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
#
#         if not user:
#             raise AuthenticationFailed('Invalid credentials, try again')
#
#         return {
#             'role': user.role,
#             'email': user.email,
#             'tokens': user.tokens,
#             'username': user.username,
#             'get_full_name': user.get_full_name,
#         }

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
