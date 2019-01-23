from django.urls import path
from . import views

urlpatterns = [
    path('main', views.ShohinTorokuView.as_view(), name='ShohinToroku'),
]
