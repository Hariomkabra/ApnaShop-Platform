from django.contrib import admin
from ecommerceapp.models import Contact,product,Order,OrderUpdate
# Register your models here.

admin.site.register(Contact)
admin.site.register(product)
admin.site.register(Order)
admin.site.register(OrderUpdate)

