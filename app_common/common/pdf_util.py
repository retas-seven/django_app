import os
from io import BytesIO
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

class PdfUtil():
    @classmethod
    def renderToPdf(cls, template_src, context_dict={}):
        template = get_template(template_src)
        html  = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(
            BytesIO(html.encode('utf-8')),
            result,
            link_callback=link_callback,
            encoding='utf-8',
        )
        
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')

        return None

def link_callback(uri, rel):
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT
    path = None

    if settings.DEBUG:
        # uriは、delivery_note_pdf.htmlの「@font-face」内の「src: url(...)」の内容が設定されている
        # デバッグ時はプロジェクトフォルダ内のstaticフォルダ内にあるfontファイルを使用する
        path = '.' + sUrl + uri
    else:
        # 本番時は「manage.py collectstatic」で本番用に配置されたfontファイルを使用する
        path = sRoot + '/' + uri

    if not os.path.isfile(path):
        raise Exception(
            '%s must start with %s' % \
            (uri, sUrl)
        )

    return path