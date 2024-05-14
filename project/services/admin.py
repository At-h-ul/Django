from django.contrib import admin
from .models import ServiceEnquiry, NewProducts, UsedProducts, OnDmndOth, OnDmndLap, OnDmndPc

# Register your models here.
class ServiceEnquiryAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'enquiry_date', 'enquiry_time', 'admin_desc']

class OnDmndLapAdmin(admin.ModelAdmin):
    list_display = ['dmndlap_brand', 'dmndlap_ram', 'dmndlap_stor', 'admin_stat']

class OnDmndPcAdmin(admin.ModelAdmin):
    list_display = ['dmndpc_proc', 'dmndpc_mobo', 'dmndpc_budg', 'admin_stat']

class OnDmndOthAdmin(admin.ModelAdmin):
    list_display = ['dmndoth_prod', 'dmndoth_desc', 'dmndoth_budg', 'admin_stat']

admin.site.register(ServiceEnquiry, ServiceEnquiryAdmin)
admin.site.register(NewProducts)
admin.site.register(UsedProducts)
admin.site.register(OnDmndLap, OnDmndLapAdmin)
admin.site.register(OnDmndPc, OnDmndPcAdmin)
admin.site.register(OnDmndOth, OnDmndOthAdmin)