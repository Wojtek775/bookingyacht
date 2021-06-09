from django import forms

from bookingyacht.models import Yacht, Marina


class YachtModelForm(forms.ModelForm):
    class Meta:
        model = Yacht
        fields = '__all__'


class MarinaModelForm(forms.ModelForm):
    class Meta:
        model = Marina
        fields = '__all__'
