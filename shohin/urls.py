from django.urls import path
from .views.shohin_list_view import ShohinListView
from .views.shohin_delete_view import ShohinDeleteView
from .views.shohin_regist_view import ShohinRegistView
from .views.shohin_update_view import ShohinUpdateView


urlpatterns = [
    path('list/', ShohinListView.as_view(), name='shohin_list_view'),
    path('delete/', ShohinDeleteView.as_view(), name='shohin_delete_view'),
    path('regist/', ShohinRegistView.as_view(), name='shohin_regist_view'),
    path('updaete/', ShohinUpdateView.as_view(), name='shohin_update_view'),
]
