from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from nohin.services.nohin_service import NohinService
from nohin.forms.nohin_form import NohinForm
# from nohin.forms.nohin_form import NohinFormset
from nohin.forms.nohin_form import NohinDetailFormset
from app_table.models import NohinDetail


class NohinRegistView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        納品登録画面-初期表示処理
        '''
        service = NohinService(self.request)
        form = NohinForm()
        formset = NohinDetailFormset(None, queryset=NohinDetail.objects.none())

        params = {
            'form': form,
            'formset': formset,
            'shohin_json': service.retrieveShohin(),
            'company_json': service.retrieveCompany(),
        }

        return render(request, 'nohin/regist.html', params)
