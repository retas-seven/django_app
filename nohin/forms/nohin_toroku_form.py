from django import forms
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory
from app_table.models import Nohin
from app_table.models import NohinDetail

# class RegistNohinForm(forms.Form):
class NohinForm(forms.ModelForm):
    '''
    納品情報登録用フォーム
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
                    'id': 'regist_nohinsaki',
                    'type': 'search',
                    'list': 'modal_company_list',
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
    納品詳細情報登録用フォーム
    '''
    class Meta:
        model = NohinDetail
        fields = {'kataban', 'price', 'amount'}
        widgets = {
            'kataban': forms.TextInput(
                attrs = {
                    'type': 'search',
                    'list': 'modal_shohin_list',
                    'class' : 'form-control form-control-lg js_modal_shohin',
                }
            ),
            'price': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': '0',
                    'class' : 'form-control form-control-lg js_modal_price',
                }
            ),
            'amount': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': '0',
                    'class' : 'form-control form-control-lg js_modal_amount',
                }
            ),
        }

NohinDetailFormset = modelformset_factory(
    NohinDetail,
    form = NohinDetailForm,
    extra = 10,
)

class NohinUpdateForm(forms.ModelForm):
    '''
    納品情報更新用フォーム
    '''
    class Meta:
        model = Nohin
        fields = {'nohin_date', 'nohinsaki', 'memo'}
        widgets = {
            'nohin_date': forms.DateInput(
                attrs = {
                    'id': 'update_nohin_date',
                    'type': 'date',
                    'style': 'width: 17rem;',
                    'class' : 'form-control form-control-lg',
                }
            ),
            'nohinsaki': forms.TextInput(
                attrs = {
                    'id': 'update_nohinsaki',
                    'type': 'search',
                    'list': 'modal_company_list',
                    'class' : 'form-control form-control-lg',
                }
            ),
            'memo': forms.Textarea(
                attrs = {
                    'id': 'update_memo',
                    'rows': '3',
                    'class' : 'form-control form-control-lg',
                }
            ),
        }

class NohinDetailUpdateForm(forms.ModelForm):
    '''
    納品詳細情報登録用フォーム
    '''
    class Meta:
        model = NohinDetail
        fields = {'kataban', 'price', 'amount'}
        widgets = {
            'kataban': forms.TextInput(
                attrs = {
                    'type': 'search',
                    'list': 'modal_shohin_list',
                    'class' : 'form-control form-control-lg js_modal_shohin',
                }
            ),
            'price': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': '0',
                    'class' : 'form-control form-control-lg js_modal_price',
                }
            ),
            'amount': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': '0',
                    'class' : 'form-control form-control-lg js_modal_amount',
                }
            ),
        }

NohinDetailUpdateFormset = modelformset_factory(
    NohinDetail,
    form = NohinDetailUpdateForm,
    extra = 10,
)





