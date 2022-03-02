from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# 作成したモデルもインポート
from .models import (BopInfoModel, ItemCategoryModel, ItemModel,
                     MenberInfoModel, PersonalCategoryModel, PersonalRateModel,
                     Post, Task)
# 作成したserializerをインポート
from .serializers import (APISerializer, ItemCategorySerializer,
                          ItemSerializer, PostSerializer, TaskSerializer,
                          UserSerializer)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # だれでもアクセス可
    permission_classes = (AllowAny,)


class PostListView(generics.ListAPIView):
    """
    一覧取得
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostRetrieveView(generics.RetrieveAPIView):
    """
    １件取得
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class TaskListView(generics.ListAPIView):
    """
    一覧取得
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


class TaskRetrieveView(generics.RetrieveAPIView):
    """
    １件取得
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


class TaskViewSet(viewsets.ModelViewSet):
    """
    CRUDができる 認証必要
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['GET'])
def dataList(request):
    queryset = ItemModel.objects.all()
    serializer = APISerializer(queryset, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def dataList(request):
#     queryset = BopInfoModel.objects.get(
        
#     )
#     serializer = APISerializer(queryset, many=True)
#     return Response(serializer.data)
