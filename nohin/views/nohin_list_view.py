from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from nohin.services.nohin_service import NohinService


class NohinListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        納品一覧画面-初期表示処理
        '''
        service = NohinService(self.request)
        params = {
            'nohin_list': service.retrieveNohinList()
        }

        return render(request, 'nohin/list.html', params)
