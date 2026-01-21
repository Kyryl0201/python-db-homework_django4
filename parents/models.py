from django.db import models

# Create your models here.
class Parent(models.Model):
    parent = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)