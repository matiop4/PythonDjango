from django import forms
from .models import Dane


class DataForm(forms.ModelForm):
    class Meta:
        model = Dane
        fields = {'rok', 'przychody', 'zysk_brutto', 'dzialalnosc_operacyjna', 'dzialalnosc_finansowa', 'zysk_netto'}
