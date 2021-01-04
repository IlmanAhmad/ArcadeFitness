from django.db import models

# Create your models here.


class Contact(models.Model):
    """Model for saving the records of Contact us forms data"""

    name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    area = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name

