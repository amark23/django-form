from django.db import models

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


class Form(models.Model):
    name = models.CharField(max_length=100,blank=False)
    date_of_birth = models.DateField(blank=False,validators=[MinAgeValidator(18)])
    email_id = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=12,blank=False)


    def __str__(self):
        return self.name #+ ' - ' + self.date_of_birth+ ' - ' +self.email_id+ ' - ' +self.phone_number
