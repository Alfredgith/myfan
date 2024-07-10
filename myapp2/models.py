from django.db import models

class who(models.Model):
      song=models.FileField(upload_to='media')
      

class pic(models.Model):
       name=models.ImageField(upload_to='media')     