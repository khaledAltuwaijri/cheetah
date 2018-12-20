from django import forms

class NameForm(forms.Form):
    song_name = forms.CharField(label='Song request', max_length=200)
