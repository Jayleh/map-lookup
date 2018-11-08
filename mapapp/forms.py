from django import forms
from django.contrib.auth import authenticate
from phonenumber_field.formfields import PhoneNumberField
from .models import Resellers, UploadFile


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


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ("file",)


class AddressForm(forms.Form):
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"id": "address-search", "data-js": "address-search",
                                      "type": "search", "placeholder": "Search Address"}),
        required=False
    )


# class RegistrationForm(forms.Form):


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_login(self, *args, **kwargs):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            elif not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            elif not user.is_active:
                raise forms.ValidationError("This user is not active")

        return super(LoginForm, self).clean(*args, **kwargs)
