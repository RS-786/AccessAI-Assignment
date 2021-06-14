from django.db import models

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)
class Employee(models.Model):
    name = models.TextField(max_length = 64)
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 1)
    salary = models.IntegerField()
    joining_date = models.DateField(auto_now = True)
    address = models.TextField(max_length = 100)

    def __str__(self):
        return self.name
