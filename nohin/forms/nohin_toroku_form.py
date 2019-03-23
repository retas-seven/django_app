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
                    'class' : 'form-control form-control-lg js_modal_change_shohin',
                }
            ),
            'price': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'min': '0',
                    'step': '1000',
                    'class' : 'form-control form-control-lg js_modal_price',
                }
            ),
            'amount': forms.TextInput(
                attrs = {
                    'type': 'number',
                    'class' : 'form-control form-control-lg',
                }
            ),
        }

NohinDetailFormset = modelformset_factory(
    NohinDetail,
    form = NohinDetailForm,
    extra = 1,
)

    # def __init__(self, request=None, *args, **kwargs):
    #     super().__init__(request, *args, **kwargs)
    #     for field in self.fields.values():
    #         # 各入力項目に「form-control form-control-lg」のCSSを適用
    #         field.widget.attrs['class'] = 'form-control form-control-lg'
    #     # 納品日の入力項目の横幅を設定
    #     self.fields.get('registNohinDate').widget.attrs['style'] = 'width: 17rem;'

    # registNohinDate = forms.DateField(
    #     label='納品日',
    #     widget=forms.DateInput(attrs={'type': 'date'}),
    # )
    # registNohinsaki = forms.CharField(
    #     label='納品先',
    #     max_length=50,
    #     widget=forms.TextInput(attrs={'type': 'search', 'list': 'modal_company_list'}),
    # )
    # registMemo = forms.CharField(
    #     label='メモ',
    #     max_length=1000,
    #     widget=forms.Textarea(attrs={'rows': '3'}),
    #     required=False,
    # )

# class UpdateNohinForm(forms.Form):
#     '''
#     納品情報更新用フォーム
#     '''
#     def __init__(self, request=None, *args, **kwargs):
#         super().__init__(request, *args, **kwargs)
#         for field in self.fields.values():
#             # 各入力項目に「form-control form-control-lg」のCSSを適用
#             field.widget.attrs['class'] = 'form-control form-control-lg'
