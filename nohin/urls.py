from django.urls import path
from . import views
from .views.nohin_list_view import NohinListView

urlpatterns = [
    path('list/', NohinListView.as_view(), name='nohin_list_view'),
    # TODO: 以下、廃止予定
    path('nohin_toroku', views.NohinTorokuView.as_view(), name='nohin_toroku'),
    path('nohin_koshin', views.NohinKoshinView.as_view(), name='nohin_koshin'),
    path('nohin_sakujo', views.NohinSakujoView.as_view(), name='nohin_sakujo'),
]
