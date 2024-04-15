from django.contrib import admin
from .models import ServiceEnquiry, NewProducts, UsedProducts, OnDmndOth, OnDmndLap, OnDmndPc

# Register your models here.
class ServiceEnquiryAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'enquiry_date', 'enquiry_time', 'admin_desc']

admin.site.register(ServiceEnquiry, ServiceEnquiryAdmin)
admin.site.register(NewProducts)
admin.site.register(UsedProducts)
admin.site.register(OnDmndLap)
admin.site.register(OnDmndPc)
admin.site.register(OnDmndOth)