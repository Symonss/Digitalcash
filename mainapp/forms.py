from django import forms

from mainapp.models import Opportunity


class OppUpdateForm(forms.ModelForm):
    class Meta :
        model = Opportunity
        fields = ['keywords','least_amount','body','status']
       