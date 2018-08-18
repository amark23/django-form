from django import forms
from .models import Form
from django.forms.widgets import DateInput
"""
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import BaseValidator
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
           ((today.month, today.day) < (born.month, born.day))

@deconstructible
class MinAgeValidator(BaseValidator):
    compare = lambda self, a, b: calculate_age(a) < b
    message = _("Age must be at least %(limit_value)d.")
    code = 'min_age'
   """
class UserForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = ['name','date_of_birth','email_id','phone_number']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }

