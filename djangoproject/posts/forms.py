from django import forms


class Resellers(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField()
    company = forms.CharField(max_length=60)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=60)
    state = forms.CharField(max_length=60)
    country = forms.CharField(max_length=60)
    lat = forms.IntegerField()
