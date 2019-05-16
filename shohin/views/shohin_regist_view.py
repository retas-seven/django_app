from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.services.shohin_toroku_service import ShohinTorokuService
from shohin.forms.shohin_toroku_form import RegistShohinForm
from shohin.forms.shohin_toroku_form import UpdateShohinForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ShohinRegistView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        商品登録画面-初期表示処理
        '''
        return render(request, 'shohin/regist.html')
