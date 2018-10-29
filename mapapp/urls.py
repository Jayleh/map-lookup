from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-reseller', views.add_reseller, name='add_reseller'),
    path('add-one-reseller', views.add_one_reseller, name='add_one_reseller'),
    path('import-resellers', views.import_resellers, name='import-resellers'),
    path('update-reseller/<id>', views.update_reseller, name='update_reseller'),
    path('reseller-data', views.reseller_data, name='reseller_data')
]
