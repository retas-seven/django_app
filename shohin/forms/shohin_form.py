from django import forms
from app_table.models import Shohin

class ShohinForm(forms.ModelForm):
    '''
    商品フォーム
    '''
    class Meta:
        model = Shohin
        fields = {'kataban', 'shohin_name', 'price', 'zaikosu', 'memo'}
        widgets = {
            'kataban': forms.TextInput(
                attrs = {
                    'class' : 'form-control form-control-lg',
                }
            ),
            'shohin_name': forms.TextInput(
                attrs = {
                    'class' : 'form-control form-control-lg',
                }
            ),
            'price': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': 0,
                    'class' : 'form-control form-control-lg',
                    'style': 'width: 17rem;'
                }
            ),
            'zaikosu': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': 0,
                    'class' : 'form-control form-control-lg',
                    'style': 'width: 17rem;'
                }
            ),
            'memo': forms.Textarea(
                attrs = {
                    'rows': '10',
                    'class' : 'form-control form-control-lg',
                }
            ),
        }




