from datetime import datetime as dt
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=dt.now(), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


class Resellers(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\d{10,15}$',
        message="Please enter phone number with only numbers (no dashes).")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.CharField(max_length=100, unique=True)
    company = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    comments = models.TextField(max_length=600)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Resellers"
