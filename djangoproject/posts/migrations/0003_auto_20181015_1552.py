# Generated by Django 2.1.2 on 2018-10-15 22:52

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_resellers_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resellers',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resellers',
            name='zipcode',
            field=localflavor.us.models.USZipCodeField(max_length=10),
        ),
    ]
