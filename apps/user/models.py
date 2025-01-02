from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100,blank=True)
    password = models.CharField(max_length=100,blank=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    goal = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title