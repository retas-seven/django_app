from django.urls import path
from .views.nohin_list_view import NohinListView
from nohin.views.nohin_regist_view import NohinRegistView
from nohin.views.nohin_update_view import NohinUpdateView
from nohin.views.nohin_delete_view import NohinDeleteView

urlpatterns = [
    path('list/', NohinListView.as_view(), name='nohin_list_view'),
    path('regist/', NohinRegistView.as_view(), name='nohin_regist_view'),
    path('delete/', NohinDeleteView.as_view(), name='nohin_delete_view'),
    path('update/', NohinUpdateView.as_view(), name='nohin_update_view'),
]
