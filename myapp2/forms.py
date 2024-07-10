from django import forms
from .models import who,pic

class mywho(forms.ModelForm):
      class Meta:
            model=who
            fields='__all__'


class mypic(forms.ModelForm):
      class Meta:
            model=pic
            fields='__all__'