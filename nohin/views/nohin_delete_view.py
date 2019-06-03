from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from nohin.services.nohin_service import NohinService
from django.contrib.auth.mixins import LoginRequiredMixin

class NohinDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        '''
        納品一覧画面-削除処理
        '''
        NohinService(request).deleteNohin(request.POST.get("nohin_id"))
        messages.success(request, '納品情報を削除しました。')
        return redirect(reverse('nohin_list_view'))
