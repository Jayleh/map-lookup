from django.db import models
from django.core.validators import EmailValidator
from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Resellers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(validators=[EmailValidator()], max_length=100, unique=True)
    phone = PhoneNumberField()
    company = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = USStateField()
    zipcode = USZipCodeField()
    comments = models.TextField(max_length=600, blank=True)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        verbose_name_plural = "Resellers"
