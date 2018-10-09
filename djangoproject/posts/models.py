from datetime import datetime as dt
from django.db import models
from django import forms
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=dt.now(), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


class Resellers(forms.Form):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    company = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    lat = models.IntegerField()
