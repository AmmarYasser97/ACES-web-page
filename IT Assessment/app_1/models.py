from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(default=18)
    def __str__(self):
        return self.first_name