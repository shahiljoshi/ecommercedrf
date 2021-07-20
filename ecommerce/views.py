from django.shortcuts import render
from .models import Category,Product,Cart,Order
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer,ProductSerializer,CartSerializer,OrderSerializer
from django.contrib.auth.models import User
from .permissions import IsCreatorOrReadOnly,IsUserOrReadOnly
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,permissions.IsAdminUser)
    # permission_classes = (IsCreatorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsCreatorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,IsUserOrReadOnly,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,IsUserOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #
    # def get_queryset(self, **kwargs):
    #     cart = Cart.objects.filter()
    #     queryset = Order.objects.filter(products=cart)
    #
    #     return queryset



class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter