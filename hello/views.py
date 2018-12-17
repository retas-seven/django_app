from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

# def index(request):
#     params = {
#         'title': 'Hello',
#         'message': 'your data:',
#         'form': HelloForm()
#     }
    
#     if (request.method == 'POST'):
#         params['message'] = '名前：' + request.POST['name'] + \
#             '<br>メール：' + request.POST['mail'] + \
#             '<br>年齢：' + request.POST['age']
#         params['form'] = HelloForm(request.POST)
        
#     return render(request, 'hello/index.html', params)

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data:',
            'form': HelloForm()
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        print(request.POST)
        msg = request.POST['name'] + '<br>' + request.POST['mail'] + '<br>' + request.POST['age']
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
