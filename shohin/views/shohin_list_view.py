from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.services.shohin_service import ShohinService
from shohin.forms.shohin_form import  ShohinForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ShohinListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        商品一覧画面-初期表示処理
        '''
        service = ShohinService(self.request)
        params = {
            'shohin_list': service.retrieveShohinList()
        }

        return render(request, 'shohin/list.html', params)
