from django.db import models

class User(models.Model):
    weight = models.IntegerField()
    height = models.IntegerField()
    goal = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title