from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ServiceEnquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product_name = models.CharField(max_length=20)
    product_manuf = models.CharField(max_length=30)
    product_issue = models.CharField(max_length=250)
    user_phone = models.CharField(max_length=10)
    user_address = models.CharField(max_length=250)
    enquiry_date = models.DateField()
    enquiry_time = models.TimeField()
    admin_desc = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.product_name

class NewProducts(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    newprod_name = models.CharField(max_length=100)
    newprod_desc = models.CharField(max_length=500)
    newprod_price = models.CharField(max_length=10)
    newprod_img = models.ImageField(upload_to ='new')

    def __str__(self):
        return self.newprod_name
    
class UsedProducts(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    usedprod_name = models.CharField(max_length=100)
    usedprod_price = models.CharField(max_length=10)
    usedprod_cond = models.CharField(max_length=20)
    usedprod_img = models.ImageField(upload_to ='old')

    def __str__(self):
        return self.usedprod_name
    
class OnDmndLap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    dmndlap_brand = models.CharField(max_length=20)
    dmndlap_model = models.CharField(max_length=20)
    dmndlap_proce = models.CharField(max_length=20)
    dmndlap_ram = models.CharField(max_length=20)
    dmndlap_stor = models.CharField(max_length=20)
    dmndlap_budg = models.CharField(max_length=10)
    admin_stat = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.dmndlap_budg

class OnDmndPc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    dmndpc_proc = models.CharField(max_length=20)
    dmndpc_mobo = models.CharField(max_length=20)
    dmndpc_ram = models.CharField(max_length=20)
    dmndpc_stor = models.CharField(max_length=20)
    dmndpc_gfx = models.CharField(max_length=20, blank=True, null=True)
    dmndpc_cab = models.CharField(max_length=20)
    dmndpc_psu = models.CharField(max_length=20)
    dmndpc_budg = models.CharField(max_length=10)
    admin_stat = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.dmndpc_budg
    
class OnDmndOth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    dmndoth_prod = models.CharField(max_length=20, blank=True, null=True)
    dmndoth_desc = models.CharField(max_length=150)
    dmndoth_budg = models.CharField(max_length=20)
    admin_stat = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.dmndoth_budg