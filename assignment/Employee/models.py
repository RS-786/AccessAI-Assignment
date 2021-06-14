from django.db import models
from django.core.exceptions import ValidationError
import copy

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)

def salary_check(salary):
    if salary<0:
        raise ValidationError("Salary cannot be negative !")
    else:
        return salary

def name_check(name):
    name_copy = copy.copy(name)
    name_copy = name_copy.replace(' ','')
    if not name_copy.isalpha():
        raise ValidationError("Name must contain alphabets only !")

    return name

class Employee(models.Model):
    name = models.CharField(max_length = 64,validators=[name_check])
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 1)
    salary = models.IntegerField(validators=[salary_check])
    joining_date = models.DateField(auto_now = True)
    address = models.TextField(max_length = 100)

    def __str__(self):
        return self.name
