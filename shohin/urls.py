from django.urls import path
from . import views
from .views.shohin_list_view import ShohinListView
from .views.shohin_delete_view import ShohinDeleteView
from .views.shohin_regist_view import ShohinRegistView


urlpatterns = [
    path('list', ShohinListView.as_view(), name='shohin_list_view'),
    path('delete', ShohinDeleteView.as_view(), name='shohin_delete_view'),
    path('regist', ShohinRegistView.as_view(), name='shohin_regist_view'),
    # TODO: 以下、廃止予定
    path('shohin_toroku', views.ShohinTorokuView.as_view(), name='shohin_toroku'),
    path('shohin_sakujo', views.ShohinSakujoView.as_view(), name='shohin_sakujo'),
    path('shohin_koshin', views.ShohinKoshinView.as_view(), name='shohin_koshin'),
]
