from django.contrib import admin
from app_1.models import Usuario
from app_1.models import Etiqueta
from app_1.models import Puntos
from app_1.models import Actividad
from app_1.models import Producto

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Etiqueta)
admin.site.register(Puntos)
admin.site.register(Actividad)
admin.site.register(Producto)
