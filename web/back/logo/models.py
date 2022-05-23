from django.db import models
from user.models import User

# Create your models here.
class Logo(models.Model) :
    image = models.ImageField(upload_to = 'logos/')
    uploader = models.ForeignKey(User, related_name='uploader', on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.uploader)