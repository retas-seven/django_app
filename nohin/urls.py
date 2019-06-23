from django.urls import path
from .views.nohin_list_view import NohinListView
from nohin.views.nohin_regist_view import NohinRegistView
from nohin.views.nohin_update_view import NohinUpdateView
from nohin.views.nohin_delete_view import NohinDeleteView
from nohin.views.delivery_note_view import DeliveryNoteView

urlpatterns = [
    path('list/', NohinListView.as_view(), kwargs={'mode': 'list'}, name='nohin_list_view'),
    path('delivery_note_list/', NohinListView.as_view(), kwargs={'mode': 'pdf_list'}, name='nohin_list_view_deivery_note'),
    path('regist/', NohinRegistView.as_view(), name='nohin_regist_view'),
    path('delete/', NohinDeleteView.as_view(), name='nohin_delete_view'),
    path('update/', NohinUpdateView.as_view(), name='nohin_update_view'),
    path('delivery_note/', DeliveryNoteView.as_view(), name='delivery_note_view'),
]
