from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    bio = models.TextField()
    image = models.ImageField(upload_to='client_image')

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
