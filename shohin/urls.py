from django.urls import path
from . import views

urlpatterns = [
    path('shohin_toroku', views.ShohinTorokuView.as_view(), name='ShohinToroku'),
]
