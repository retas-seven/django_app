from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from nohin.services.nohin_service import NohinService
from nohin.forms.nohin_form import NohinForm
from nohin.forms.nohin_form import NohinDetailFormset
from app_table.models import NohinDetail


class NohinUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        納品更新画面-初期表示処理
        '''
        nohinId = request.GET['nohin_id']
        service = NohinService(request)
        nohin = service.retrieveNohin(nohinId)
        
        if not nohin:
            messages.error(request, '納品情報の取得に失敗しました。')
            return redirect(reverse('nohin_list_view'))

        form = NohinForm(list(nohin)[0])
        formset = NohinDetailFormset(None, queryset=service.retrieveNohinDetailList(nohinId))

        params = {
            'mode': 'update',
            'form': form,
            'formset': formset,
            'shohin_json': service.retrieveShohin(),
            'company_json': service.retrieveCompany(),
            'update_nohin_id': nohinId,
        }

        return render(request, 'nohin/regist.html', params)

    def post(self, request, *args, **kwargs):
        '''
        納品更新画面-更新処理
        '''
        nohinId = request.POST['update_nohin_id']
        service = NohinService(request)

        nohin = service.retrieveNohinModel(nohinId)
        nohinDetails = service.retrieveNohinDetailModelByNohin(nohin)

        form = NohinForm(request.POST, instance=nohin)
        formset = NohinDetailFormset(request.POST, queryset=nohinDetails)

        if not form.is_valid() or not formset.is_valid():
            params = {
                'mode': 'update',
                'form': NohinForm(request.POST),
                'formset': NohinDetailFormset(request.POST),
                'shohin_json': service.retrieveShohin(),
                'company_json': service.retrieveCompany(),
                'update_nohin_id': nohinId,
            }
            return render(request, 'nohin/regist.html', params)

        # 納品を登録する
        service.updateNohin(form, formset)
        service.registCompany(form.cleaned_data['nohinsaki'])
        messages.success(request, '納品情報を更新しました。')
        
        # 納品一覧画面の初期表示処理へリダイレクト
        return redirect(reverse('nohin_list_view'))
