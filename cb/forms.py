from django import forms
from .models import Rps

class RpsForm(forms.Form):
    def __init__(self,*args, **kwargs):
        self.book_id = kwargs.pop('book_id')
        super(RpsForm,self).__init__(*args, **kwargs)

    forms.CharField(max_length=30,label='name')
    forms.IntegerField(label='start')
    forms.IntegerField(label='end')

