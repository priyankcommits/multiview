from django import forms


class ImageDetailForm(forms.Form):
    image = forms.ImageField()
