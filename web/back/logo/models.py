from django.db import models

# Create your models here.
class Logo(models.Model) :
    image = models.ImageField(upload_to = 'logos/', null=True)
    video = models.FileField(upload_to= 'videos/', null=True)

    def __str__(self):
        return "{0}".format(self.image)

class LogoResult(models.Model):
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE)
    result = models.FileField(upload_to = 'results/', null = True)

    def __str__(self):
        return "{0}".format(self.logo)
    