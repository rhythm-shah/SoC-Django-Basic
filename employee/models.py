from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=5)
    employee_name = models.CharField(max_length=100)
    employee_salary = models.CharField(max_length=10)
    employee_age = models.CharField(max_length=2)
    profile_img = models.CharField(max_length=1000, null=True)   #for url of img
    objects = models.Manager()
    def __str__(self):
        return self.employee_id + ' - ' + self.employee_name + ' - ' + self.employee_salary + ' - ' + self.employee_age