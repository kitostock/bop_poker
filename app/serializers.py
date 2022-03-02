from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ItemCategoryModel, ItemModel, Post, Task


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategoryModel
        fields = ['id', 'item_category_name']
 
class ItemSerializer(serializers.ModelSerializer):
    item_category_name = serializers.ReadOnlyField(
        source='item_category_id.item_category_name', 
        read_only=True)
 
    class Meta:
        model = ItemModel
        fields = ['id', 'item_name', 'item_category_id', 'item_category_name']


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel # 使用するモデル
        fields = '__all__' # 処理対象にするフィールド（今回は全項目）
