from django.db import models
from django.utils import timezone

# Create your models here.
class Multimedia(models.Model):
    nombre = models.CharField(max_length=50)
    video = models.FileField(upload_to ='videos', null=False, blank=True)
    foto = models.ImageField(upload_to ='videos', null=False, blank=True)
    fecha_publicacion = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.nombre

