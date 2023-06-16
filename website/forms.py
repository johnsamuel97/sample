from django import forms
from django.contrib.auth.models import User
from website.models import Record

class Sign_up(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name'] 
class Insert_record(forms.ModelForm):
    class Meta:
        model=Record
        fields="__all__"