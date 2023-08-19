from . import views
from django.urls import path,include

urlpatterns = [
    path('register',views.register,name='register'),
    path('', views.login, name='login'),
    path('index',views.index,name='index'),
    path('videocall', views.videocall, name='videocall'),
    path('join', views.join, name='join'),
]