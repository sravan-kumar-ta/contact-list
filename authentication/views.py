import jwt
from django.conf import settings
from django.contrib import auth
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import Contact
from authentication.serializers import UserSerializer, ContactSerializer


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(GenericAPIView):
#     def post(self, request):
#         data = request.data
#         username = data.get('username', '')
#         password = data.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#
#         if user:
#             auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
#
#             serializer = UserSerializer(user)
#
#             data = {
#                 'user': serializer.data,
#                 'token': auth_token
#             }
#             return Response(data, status=status.HTTP_200_OK)
#
#         return Response({'detail': 'Invalid credentials..'}, status=status.HTTP_401_UNAUTHORIZED)


class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
