from django import forms
from django.forms import modelformset_factory
from app_table.models import Nohin
from app_table.models import NohinDetail

class NohinForm(forms.ModelForm):
    '''
    納品フォーム
    '''
    class Meta:
        model = Nohin
        fields = {'nohin_date', 'nohinsaki', 'memo'}
        widgets = {
            'nohin_date': forms.DateInput(
                attrs = {
                    'id': 'regist_nohin_date',
                    'type': 'date',
                    'style': 'width: 17rem;',
                    'class' : 'form-control form-control-lg',
                }
            ),
            'nohinsaki': forms.TextInput(
                attrs = {
                    # 'id': 'regist_nohinsaki',
                    'type': 'search',
                    'list': 'company_list',
                    'class' : 'form-control form-control-lg',
                }
            ),
            'memo': forms.Textarea(
                attrs = {
                    'id': 'regist_memo',
                    'rows': '3',
                    'class' : 'form-control form-control-lg',
                }
            ),
        }

class NohinDetailForm(forms.ModelForm):
    '''
    納品詳細フォーム
    '''
    class Meta:
        model = NohinDetail
        fields = {'kataban', 'price', 'amount'}
        widgets = {
            'kataban': forms.TextInput(
                attrs = {
                    'type': 'search',
                    'list': 'shohin_list',
                    'class' : 'form-control form-control-lg js_shohin',
                }
            ),
            'price': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': '0',
                    'class' : 'form-control form-control-lg js_price',
                }
            ),
            'amount': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': '0',
                    'class' : 'form-control form-control-lg js_amount',
                }
            ),
        }

NohinDetailFormset = modelformset_factory(
    NohinDetail,
    form = NohinDetailForm,
    extra = 5,
    max_num = 5,
    can_delete = True,
)
