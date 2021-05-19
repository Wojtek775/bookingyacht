from django import forms

from bookingyacht.models import Yacht


class YachtModelForm(forms.ModelForm):
    class Meta:
        model = Yacht
        fields = '__all__'
