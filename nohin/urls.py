from django.urls import path
from . import views

urlpatterns = [
    path('nohin_toroku', views.NohinTorokuView.as_view(), name='nohin_toroku'),
    path('nohin_koshin', views.NohinKoshinView.as_view(), name='nohin_koshin'),
]
