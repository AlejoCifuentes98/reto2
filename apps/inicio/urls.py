from django.urls import path
from .views import *

urlpatterns = [
    #Pagina de inicio de todas las canciones
    path('archivos/', archivos_view, name='archivos'),

    #Urls de autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registrar/', registrar_view, name='registrar'),

    #Urls del artista
    path('mis_archivos/', mis_archivos_view, name='mis_archivos'),
    path('archivo_editar/<int:id_archivo>/', archivo_editar_view, name='archivo_editar'),
    path('archivo_ver/<int:id_archivo>/', archivo_ver_view, name='archivo_ver'),
    path('archivo_agregar/', archivo_agregar_view, name='archivo_agregar'),
    path('archivo_eliminar/<int:id_archivo>/', archivo_eliminar_view, name='archivo_eliminar'),
]