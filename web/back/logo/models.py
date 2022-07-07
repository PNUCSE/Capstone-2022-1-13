from django.db import models

# Create your models here.
class Logo(models.Model) :
    image = models.ImageField(upload_to = 'logos/')

    def __str__(self):
        return "{0}".format(self.image)