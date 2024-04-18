from django.db import models

# Create your models here.
class WebsiteDetails(models.Model):
    web_about = models.TextField()
    web_contact = models.TextField()