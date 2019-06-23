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
        path = 'static/resources/font/GenYoMinJP-Regular.ttf'
        # print('----------------')
        # print(uri)
        # print(path)
        # print('----------------')
    else:
        path = os.path.join('static', uri)

    if not os.path.isfile(path):
        # print('----------------')
        # print('fontファイルが存在しない')
        # print('----------------')
        raise Exception(
            '%s must start with %s' % \
            (uri, sUrl)
        )

    # print('----------------')
    # print(uri)
    # print(sUrl)
    # print(sRoot)
    # print(path)
    # print('----------------')
    return path