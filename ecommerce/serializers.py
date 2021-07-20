from itertools import product

from rest_framework import serializers
from .models import Category,Product,Cart,Order
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','name','category','price','imageUrl','status','date_created','created_by')
        model = Product


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'products',)


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CartSerializer(serializers.ModelSerializer):
    total_item_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'products', 'quantity', 'total_item_price')


    def get_total_item_price(self, obj):
        return obj.get_total_item_price()


class OrderSerializer(serializers.ModelSerializer):
    # order_items = serializers.SerializerMethodField()
    # products = serializers.PrimaryKeyRelatedField(queryset=Cart.products.(Order.user))
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'address', 'ordered_date', 'total',)


    # def get_order_items(self, obj):
    #
    #     cart = Cart.objects.filter(user=1)
    #     orders = Order.objects.filter(products=cart)
    #     return orders

    def get_total(self, obj):
        return obj.get_total()
