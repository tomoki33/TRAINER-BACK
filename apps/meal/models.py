from django.db import models

class Meal(models.Model):
    # user_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    meal_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title