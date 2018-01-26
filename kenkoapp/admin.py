from django.contrib import admin
from kenkoapp.models import Carepro, Customer, Care, Order, OrderDetails, Caregiver

# Register your models here.
admin.site.register(Carepro)
admin.site.register(Caregiver)
admin.site.register(Customer)
admin.site.register(Care)
admin.site.register(Order)
admin.site.register(OrderDetails)
