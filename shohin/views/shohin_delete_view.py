from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.services.shohin_toroku_service import ShohinTorokuService
from shohin.forms.shohin_toroku_form import RegistShohinForm
from shohin.forms.shohin_toroku_form import UpdateShohinForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ShohinDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        '''
        商品一覧画面-削除処理
        '''
        ShohinTorokuService(request).deleteShohin(request.POST.get("kataban"))
        messages.success(request, '商品情報を削除しました。')
        return redirect(reverse('shohin_list_view'))
