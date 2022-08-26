from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    #  Since the Django admin will be default pluralize
    #  the app name to Citys we'll also set 
    #  verbose_name_plural
    class Meta:
        verbose_name_plural = 'Cities'

    # __str__ to display the name of the city
    def __str__(self):
        return self.name

