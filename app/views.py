from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
# 作成したserializerをインポート
from .serializers import ItemCategorySerializer, ItemSerializer
# 作成したモデルもインポート
from .models import ItemCategoryModel, ItemModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import APISerializer

@api_view(['GET']) # GET のみに対応 
def dataList(request):
    queryset = ItemModel.objects.all()
    serializer = APISerializer(queryset, many=True)
    return Response(serializer.data)
