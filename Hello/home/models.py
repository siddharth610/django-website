from django.db import models

# make migrations - create change and store ina file
# migrate - apply the chnage created by makemigrations

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    desc =models.TextField()
    date =models.DateField()

    def __str__(self):
        return self.name + " " + self.email