from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User

class agregar_archivo_form (forms.ModelForm):
    class Meta:
        model = Archivo
        fields = '__all__'
class login_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput()) # input TEXT html
    clave   = forms.CharField(widget=forms.PasswordInput(render_value=False)) # input PASSWROD html

class registrar_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput())
    correo  = forms.EmailField(widget=forms.TextInput())
    clave_1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(render_value= False))
    clave_2 = forms.CharField(label='Confirme la Contraseña',widget=forms.PasswordInput(render_value= False))
    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        try:
            u = User.objects.get(username =usuario)     
        except User.DoesNotExist:
            return usuario
        raise forms.ValidationError('Éste usuario ya existe, por favor intente con otro')    

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        try:
            u = User.objects.get(email =correo)     
        except User.DoesNotExist:
            return correo
        raise forms.ValidationError('Éste correo ya existe, por favor intente con otro')

    def clean_clave_2(self):
        clave_1 = self.cleaned_data['clave_1']
        clave_2 = self.cleaned_data['clave_2']
        if clave_1 == clave_2:
            return clave_2
        else:
            raise forms.ValidationError('Las contraseñas no coinciden, por favor verifique')        