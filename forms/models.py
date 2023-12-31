from django.db import models

class DigitalForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField
    birth_place = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
