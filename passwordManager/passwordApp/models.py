from django.db import models
from django.contrib.auth.models import User
import bcrypt

# Create your models here.
class PassWordManagerDataModel(models.Model):
    userName = models.CharField(max_length=100)
    websiteName = models.CharField(max_length=100)
    websiteUrl = models.URLField(blank=True, default='')
    password = models.CharField(max_length=100)

    def get_username(self):
        return self.userName

    def set_username(self, username):
        self.userName = username

    def get_website_name(self):
        return self.websiteName

    def set_website_name(self, website_name):
        self.websiteName = website_name

    def set_password(self, raw_password):
        hashed = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed.decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))
    
    def get_website_data(self):
        return [self.websiteName, self.websiteUrl, self.password]
    
    def set_website_data(self, website_name, website_url, raw_password):
        self.websiteName = website_name
        self.websiteUrl = website_url
        hashed = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed.decode('utf-8')
class SafeBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    password_manager_data = models.ManyToManyField(PassWordManagerDataModel)