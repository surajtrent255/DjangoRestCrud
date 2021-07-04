
from django.db import models
class EmployeeModel(models.Model):
    empName = models.CharField(max_length=100)
    email = models.CharField(max_length = 100)
    salary = models.IntegerField()

    def __str__(self):
        return self.empName + " (" + self.email+ ")"
