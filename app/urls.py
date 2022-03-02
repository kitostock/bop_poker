from app.views import (CreateUserView, PostListView, PostRetrieveView,
                       TaskListView, TaskRetrieveView, TaskViewSet)
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

# app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('data-list/', views.dataList, name="data-list"),
    # path('bop-infos/find-one/', views.dataList, name="bop-infos-find-one"),
]
