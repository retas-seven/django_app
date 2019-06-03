from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from nohin.services.nohin_service import NohinService


class NohinRegistView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        納品登録画面-初期表示処理
        '''
        return render(request, 'nohin/regist.html', {})
