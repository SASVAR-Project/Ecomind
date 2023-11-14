from django.db import models

# Create your models here.

class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True, blank=False)
	nombre = models.CharField(max_length=45, null=False)
	total_puntos = models.PositiveIntegerField(default=0)

class Etiqueta(models.Model):
	id_archivo = models.CharField(max_length=150, null = True, blank=False)
	Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
	fecha_etiquetado = models.DateTimeField(auto_now_add=True)
	Material = models.CharField(max_length=45, null = True, blank=False)
	Package_color = models.CharField(max_length=45, null = True, blank=False)
	Bottle_cap = models.CharField(max_length=45, null=True, blank=False)
	Dirtiness = models.CharField(max_length=45, null=True, blank=False)
	Packaging_type = models.CharField(max_length=45, null=True, blank=False)
	Brand = models.CharField(max_length=45, null=True, blank=False)
	Reference = models.CharField(max_length=45, null=True, blank=False)
	Capacity = models.CharField(max_length=45, null=True, blank=False)
	Damage = models.CharField(max_length=45, null=True, blank=False)

class Puntos(models.Model):
	Usuario_id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
	cantidad_puntos = models.IntegerField(default=0)
	fecha_puntos = models.DateTimeField(auto_now_add=True)

class Actividad(models.Model):
	Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
	tipo_actividad = models.CharField(max_length=45, null=False, blank=False, choices=(('etiquetado','etiquetado'),('clasificado','clasificado'), ('canjeo','canjeo')))
	fecha_actividad = models.DateTimeField(auto_now_add=True)

class Clasificacion(models.Model):
	Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
	id_archivo = models.CharField(max_length=150, null = True, blank=False)
	fecha_actividad = models.DateTimeField(auto_now_add=True)

class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True, blank=False)
	nombre_producto = models.CharField(max_length=45, null=False)
	imagen = models.CharField(max_length=1000, null=False)
	descripcion = models.CharField(max_length=1000, null=False)
	costo = models.PositiveIntegerField(default=0)
	stock = models.PositiveIntegerField(default=0)

#python manage.py makemigrations
#python manage.py sqlmigrate app_1 0001
#python manage.py migrate

#python manage.py shell
#from app_1.models import Usuarios
#usr5 = Usuarios(codigo = 'AAA000', nombre = 'Esteban Trujillo', cantidadRecogida = 25)