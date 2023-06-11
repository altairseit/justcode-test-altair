from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet,mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import TokenObtainPairSerializer, TokenRefreshSerializer, ProductCardSerializer,UserSerializer, GetUserSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .models import User, ProductCard
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .permissions import IsCourier

class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenObtainPairSerializer

class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenRefreshSerializer

class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes=[AllowAny]
    serializer_class=UserSerializer