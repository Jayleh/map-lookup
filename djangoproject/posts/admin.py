from django.contrib import admin

# Register your models here.
from .models import Posts, Resellers

admin.site.register(Posts)
admin.site.register(Resellers)
