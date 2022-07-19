from django.db import models

# Create your models here.
class Logo(models.Model) :
    image = models.ImageField(upload_to = 'logos/', null=True)
    video = models.FileField(upload_to= 'videos/', null=True)

    def __str__(self):
        return "{0}".format(self.image)