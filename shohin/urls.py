from django.urls import path
from . import views

urlpatterns = [
    path('shohin_toroku', views.ShohinTorokuView.as_view(), name='shohin_toroku'),
    path('shohin_sakujo', views.ShohinSakujoView.as_view(), name='shohin_sakujo'),
]
