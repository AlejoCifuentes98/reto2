from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
'''class P_claves (models.Model):
    palabras = models.CharField(max_length=500)
    def __str__(self):
        return self.palabras
'''
    
class Archivo(models.Model):
    nombres = models.CharField(max_length=500)
    apellidos = models.CharField(max_length=500)
    archivo = models.FileField(upload_to='videos', null=True,blank=True)
    foto = models.ImageField(upload_to='fotos', null=True,blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    def nombre_completo(self):
        return self.nombre + ''+ self.apellidos

    
    '''def get_by_fecha_publicacion(self, fecha_publicacion):
        return queryset.filter(created_at__date__range=(start_date, end_date))
    '''
    '''objects = VideoManager()'''


    '''def publicacion(self):
        self.fecha_publicacion  = timezone.now()
        self.save()'''
    
    '''class Meta: 
     ordering = ('-datetime') 
'''
    