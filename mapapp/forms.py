from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Resellers


class ResellerForm(forms.ModelForm):
    phone = PhoneNumberField(initial="+1")

    class Meta:
        model = Resellers
        fields = ("first_name", "last_name", "email", "phone", "company",
                  "address", "city", "state", "zipcode", "comments")
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "E-mail",
            "zipcode": "ZIP/Postal Code"
        }
        widgets = {
            "comments": forms.Textarea(attrs={"class": "materialize-textarea"})
        }


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
