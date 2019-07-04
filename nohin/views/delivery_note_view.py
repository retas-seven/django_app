from decimal import Decimal, ROUND_DOWN
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import get_template
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from app_common.common.pdf_util import PdfUtil
from datetime import datetime
from nohin.services.nohin_service import NohinService
from nohin.forms.nohin_form import NohinForm
from nohin.forms.nohin_form import NohinDetailFormset


class DeliveryNoteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        '''
        納品書PDFをダウンロードする
        '''
        params, fileName = self.retrieveNohinData()
        template = get_template('nohin/delivery_note_pdf.html')
        html = template.render(params)
        pdf = PdfUtil.renderToPdf('nohin/delivery_note_pdf.html', params)
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(fileName)

            if not request.GET.get("preview"):
                content = "attachment; filename=%s" %(fileName)

            response['Content-Disposition'] = content
            return response

        return HttpResponse("Not found")

    def retrieveNohinData(self):
        nohinId = self.request.GET['nohin_id']
        # nohinId = 45
        totalPrice = 0
        service = NohinService(self.request)
        nohin = service.retrieveNohin(nohinId)
        
        if not nohin:
            messages.error(self.request, '納品情報の取得に失敗しました。')
            return redirect(reverse('nohin_list_view'))

        nohin = list(nohin)[0]
        detailList = [detail.__dict__ for detail in service.retrieveNohinDetailList(nohinId)]
        
        # 合計金額を計算
        for detail in detailList:
            detail['item_total'] = detail.get('price') * detail.get('amount')
            totalPrice = totalPrice + detail.get('item_total')
        zeigaku = (Decimal(totalPrice) * Decimal('0.08')).quantize(Decimal('0'), rounding=ROUND_DOWN)  # TODO: 税額計算を共通化
        nohin['total_price'] = totalPrice
        nohin['zeigaku'] = zeigaku
        nohin['zeikomi_total_price'] = zeigaku + totalPrice

        params = {
            'nohin': nohin,
            'detailList': detailList,
        }

        # TODO: ファイル名を日本語にする
        # fileName = f'納品書_{nohin.get("nohinsaki")}'
        fileName = 'delivery_note.pdf'

        return params, fileName