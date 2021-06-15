from django.db import models
from django.core.exceptions import ValidationError
import copy

# Employee gender choices to choose from
GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)

# Validator to check whether salary is a positive integer or not
def salary_check(salary):
    if salary<0:
        raise ValidationError("Salary cannot be negative !")
    else:
        return salary

# Creating a copy of name, getting rid of spaces and checking whether it is alphabetic or not
def name_check(name):
    name_copy = copy.copy(name)
    name_copy = name_copy.replace(' ','')
    if not name_copy.isalpha():
        raise ValidationError("Name must contain alphabets only !")

    return name

# The main employee model for this app
# Several validators are used for each field

class Employee(models.Model):
    name = models.CharField(max_length = 64,validators=[name_check], unique = True) # unique = true signifies primary key
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 1)
    salary = models.IntegerField(validators=[salary_check])
    joining_date = models.DateField(auto_now = True)
    address = models.TextField(max_length = 100)

    def __str__(self):
        return self.name
