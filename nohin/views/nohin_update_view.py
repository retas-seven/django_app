from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class NohinUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        納品更新画面-初期表示処理
        '''
        # TODO:処理を作成
        return redirect(reverse('nohin_list_view'))
