from django import forms
from .models import Resellers


class ResellerForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(max_length=17)
    company = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    zipcode = forms.CharField(label="ZIP/Postal Code", max_length=5)
    state = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    comments = forms.CharField(widget=forms.Textarea(
        attrs={"class": "materialize-textarea"}), max_length=600)

    class Meta:
        model = Resellers
        fields = ("first_name", "last_name", "email", "phone", "company",
                  "address", "city", "zipcode", "state", "country", "comments")
