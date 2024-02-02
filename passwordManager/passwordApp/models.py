from django.db import models

# Create your models here.
import datetime
from django.db import models

# Create your models here.
class PassWordManagerDataModel(models.Model):
    userName = models.CharField(max_length=100)
    websiteName = models.CharField(max_length=100)
    websiteUrl = models.URLField(blank=True, default='')
    password = models.CharField(max_length=100)