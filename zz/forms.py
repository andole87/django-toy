from django import forms
from .models import MyPDF
from django.core.exceptions import ValidationError


class RPSForm(forms.ModelForm):

    class Meta:
        model = MyPDF
        fields = ('my_origin','my_name','my_start','my_end')
