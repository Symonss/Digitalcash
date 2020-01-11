from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from mainapp.models import Opportunity, User




class OppUpdateForm(forms.ModelForm):
    class Meta :
        model = Opportunity
        fields = ['keywords','least_amount','body','status']
       