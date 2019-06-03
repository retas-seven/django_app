from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.services.shohin_service import ShohinService
from django.contrib.auth.mixins import LoginRequiredMixin

class ShohinDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        '''
        商品一覧画面-削除処理
        '''
        ShohinService(request).deleteShohin(request.POST.get("kataban"))
        messages.success(request, '商品情報を削除しました。')
        return redirect(reverse('shohin_list_view'))
