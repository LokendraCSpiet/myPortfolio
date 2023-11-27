from django.db import models

# Create your models here.

class pf_contact(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    message = models.CharField(max_length=200)