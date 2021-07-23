from django import forms
from .models import matlabs
from django.forms import ModelForm
from . import models


#class contactform(forms.Form):
  #  form_email = forms.EmailField(required=True)
   # subject = forms.CharField(required=True)
   # message = forms.CharField(widget=forms.Textarea, required=True)

class matlabform(ModelForm):
    class Meta:
       model = models.matlabs
       fields = ('title','mohtava')