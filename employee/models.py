from django.db import models # type: ignore

# Create your models here.

class Employee(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    employee_id = models.IntegerField()
    dob = models.DateField()
    joining_date = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    designation = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    class Meta:
        ordering = ('employee_id',)
    

