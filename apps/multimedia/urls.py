from django.urls import path
from .views import *

urlpatterns = [
    #Pagina de inicio de todas las canciones
    path('', archivos_view, name='archivos'),

    #Urls de autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registrar/', registrar_view, name='registrar'),

    #Urls del artista
    
]