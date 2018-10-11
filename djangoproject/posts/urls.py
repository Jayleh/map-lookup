from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-reseller', views.add_reseller, name='add_reseller')
]
