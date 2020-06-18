from .models import Postcard

from django import forms


class SubmitLuvLetterForm(forms.Form):
    author = forms.CharField(label='name', max_length=100)
    letter = forms.TextField(label='luv-letter-input')

