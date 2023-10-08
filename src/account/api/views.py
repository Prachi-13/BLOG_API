"""Class based view for Account"""
from django.db import transaction
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from account.api.serializers import UserPublicSerializer, UserRegisterSerializer, UserSerializer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from framework.permissions import IsStaffOrUserOrReadOnly, IsUserOrReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

User = get_user_model()

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    name = 'user-list'
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    name = 'user-detail'
    permission_classes = (IsUserOrReadOnly | IsAdminUser, )
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class UserRegisterAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserRegisterSerializer
    name = 'user_register'

    def get(self, request, format=None):
        serializer = self.serializer_class()
        return Response(data=serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            email = request.data.get('email')
            subject = "Account Created !"
            message = f'Dear {new_user}, Your account has been created.'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            return Response(data={'success':True, 'message': 'Account created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
