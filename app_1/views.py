
from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import *

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

id2 = 1


# Create your views here.
def creditos(request):
    return render(request, 'creditos.html')
    
def registro(request):
    if request.user.is_authenticated:
        return redirect('../home/')
    else:
        class CreateUserForm(UserCreationForm):
            class Meta:
                model = User
                fields = ['username', 'password1', 'password2']
        form = CreateUserForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                pwd = form.cleaned_data.get('password1')
                messages.success(request, 'La cuenta fue creada')
                messages.success(request, 'satisfactoriamente para ' + user)
                usuarioN = Usuario(nombre=user)
                usuarioN.save()
                user2 = authenticate(request, username=user, password=pwd)
                login(request, user2)
                return redirect('../home/')
                
        context = {'form': form}
        return render(request, 'registro.html', context)


def login1(request):
    if request.user.is_authenticated:
        return redirect('../home/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../home/')
            else:

                messages.info(request, 'Nombre de usuario o contraseña')
                messages.info(request, 'están incorrectos')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('../login/')


@login_required(login_url='../login/')
def home(request):
    usuarios_obj = Usuario.objects.get(nombre=request.user)
    return render(request, 'home.html', {'nombre': usuarios_obj.nombre})


@login_required(login_url='../login/')
def mis_puntos(request):
    usuarios_obj = Usuario.objects.get(nombre=request.user)
    puntos_todos = Puntos.objects.filter(
        Usuario_id_usuario_id=usuarios_obj.id_usuario)
    return render(request, 'mis_puntos.html', {'puntos_todos': puntos_todos, 'total_puntos': usuarios_obj.total_puntos, 'nombre': usuarios_obj.nombre})


@login_required(login_url='../login/')
def tienda(request):
    productos = Producto.objects.all()
    usuarios_obj = Usuario.objects.get(nombre=request.user)
    puntos_todos = Puntos.objects.filter(Usuario_id_usuario_id=usuarios_obj.id_usuario)
    try:
        prod = request.POST['producto_elegido']

    except:
        if puntos_todos == 1:
            return render(request, 'tienda.html', { 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " punto", 'nombre': usuarios_obj.nombre})
        else:
            return render(request, 'tienda.html', { 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " puntos", 'nombre': usuarios_obj.nombre})
    else:
        product = Producto.objects.get(id_producto = prod)
        if product.stock > 0 and usuarios_obj.total_puntos >= product.costo:
            usuarios_obj.total_puntos = usuarios_obj.total_puntos - product.costo
            usuarios_obj.save()
            product.stock = product.stock - 1
            product.save()
            db_actividad2 = Actividad(
                Usuario_id_usuario_id=usuarios_obj.id_usuario, tipo_actividad='canjeo')
            db_actividad2.save()
            db_puntos2 = Puntos(cantidad_puntos= int("-"+str(product.costo)),
                               Usuario_id_usuario_id=usuarios_obj.id_usuario)
            db_puntos2.save()
            mensaje = "¡Has adquirido satisfactoriamente tu incentivo!"
            if puntos_todos == 1:
                return render(request, 'tienda.html', {'mensaje': mensaje, 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " punto", 'nombre': usuarios_obj.nombre})
            else:
                return render(request, 'tienda.html', {'mensaje': mensaje, 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " puntos", 'nombre': usuarios_obj.nombre})
        elif product.stock == 0:
            mensaje = "Lo sentimos, no hay existencias disponibles del producto que seleccionaste."
            if puntos_todos == 1:
                return render(request, 'tienda.html', {'mensaje': mensaje, 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " punto", 'nombre': usuarios_obj.nombre})
            else:
                return render(request, 'tienda.html', {'mensaje': mensaje, 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " puntos", 'nombre': usuarios_obj.nombre})
        elif usuarios_obj.total_puntos < product.costo:
            falta = product.costo - usuarios_obj.total_puntos
            if falta == 1:
                mensaje = "Lo sentimos, no tienes puntos suficientes. Te falta " + str(falta) + " punto."
            else:
                mensaje = "Lo sentimos, no tienes puntos suficientes. Te faltan " + str(falta) + " puntos."
            if puntos_todos == 1:
                return render(request, 'tienda.html', {'mensaje': mensaje, 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " punto", 'nombre': usuarios_obj.nombre})
            else:
                return render(request, 'tienda.html', {'mensaje': mensaje, 'productos': productos, 'puntos_todos': puntos_todos, 'total_puntos': str(usuarios_obj.total_puntos) + " puntos", 'nombre': usuarios_obj.nombre})
       


@login_required(login_url='../login/')
def mi_actividad(request):
    usuarios_obj = Usuario.objects.get(nombre=request.user)
    actividades = Actividad.objects.filter(
        Usuario_id_usuario_id=usuarios_obj.id_usuario)
    return render(request, 'mi_actividad.html', {'actividades': actividades, 'nombre': usuarios_obj.nombre})


@login_required(login_url='../login/')
def etiquetado(request):
    return render(request, 'etiquetado.html')


@login_required(login_url='../login/')
def realizar_etiquetado(request):
    return render(request, 'realizar_etiquetado.html')


@login_required(login_url='../login/')
def clasificado(request):
    return render(request, 'clasificado.html')


@login_required(login_url='../login/')
def clasificado_etiqueta(request):
    usuarios_obj3 = Usuario.objects.get(nombre=request.user)
    etiquetas = Etiqueta.objects.filter(Usuario_id_usuario_id=usuarios_obj3.id_usuario)

    try:
        archivo = request.POST['archivo']
    except:
        archivo = 0
        enlace_caneca = "https://rimoplasticas.com/wp-content/uploads/2020/12/colores-de-la-caneca-de-reciclaje.jpg"
        return render(request, 'clasificado_etiqueta.html', {'archivo': "...", 'enlace': enlace_caneca, 'etiquetas':etiquetas})
    else:
        caneca = ""
        cpuntos = 0
        enlace_caneca = ""
        
        archivo2= Etiqueta.objects.get(id=int(archivo))

        if archivo2.Capacity != "N/A":
            capacidad = archivo2.Capacity + " ml"
        else:
            capacidad = archivo2.Capacity
        if archivo2.Material == "Other plastic":
            caneca = "caneca negra (residuos no aprovechables)"
            enlace_caneca = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"

            cpuntos = 1

        elif archivo2.Dirtiness == "Clean" and archivo2.Damage == "Undamaged":
            if archivo2.Material == 'PET':
                cpuntos = 2
            elif archivo2.Material == 'PE-HD':
                cpuntos = 6
            elif archivo2.Material == 'PVC':
                cpuntos = 7
            elif archivo2.Material == 'PE-LD':
                cpuntos = 4
            elif archivo2.Material == 'PP':
                cpuntos = 2
            elif archivo2.Material == 'PS':
                cpuntos = 2
            elif archivo2.Material == 'Other plastic':
                cpuntos = 1
            elif archivo2.Material == 'Glass':
                cpuntos = 2
            elif archivo2.Material == 'Aluminium':
                cpuntos = 17
            elif archivo2.Material == 'Other metal':
                cpuntos = 1
            elif archivo2.Material == 'Cardboard':
                cpuntos = 2
            elif archivo2.Material == 'Paper print':
                cpuntos = 1
            elif archivo2.Material == 'Newspaper':
                cpuntos = 2
            elif archivo2.Material == 'Magazine':
                cpuntos = 2
            elif archivo2.Material == 'Tetrapack':
                cpuntos = 2
            elif archivo2.Material == 'Other':
                cpuntos = 1

            caneca = "caneca blanca (residuos aprovechables)"
            enlace_caneca = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"

        elif archivo2.Dirtiness != "Clean":
            cpuntos = 1

            caneca = "caneca negra (residuos no aprovechables)"
            enlace_caneca = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"

        elif archivo2.Dirtiness == "Clean" and archivo2.Material != "Glass":

            if archivo2.Material == 'PET':
                cpuntos = 2
            elif archivo2.Material == 'PE-HD':
                cpuntos = 6
            elif archivo2.Material == 'PVC':
                cpuntos = 7
            elif archivo2.Material == 'PE-LD':
                cpuntos = 4
            elif archivo2.Material == 'PP':
                cpuntos = 2
            elif archivo2.Material == 'PS':
                cpuntos = 2
            elif archivo2.Material == 'Other plastic':
                cpuntos = 1
            elif archivo2.Material == 'Aluminium':
                cpuntos = 17
            elif archivo2.Material == 'Other metal':
                cpuntos = 1
            elif archivo2.Material == 'Cardboard':
                cpuntos = 2
            elif archivo2.Material == 'Paper print':
                cpuntos = 1
            elif archivo2.Material == 'Newspaper':
                cpuntos = 2
            elif archivo2.Material == 'Magazine':
                cpuntos = 2
            elif archivo2.Material == 'Tetrapack':
                cpuntos = 2
            elif archivo2.Material == 'Other':
                cpuntos = 1

            caneca = "caneca blanca (residuos aprovechables)"
            enlace_caneca = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"

        elif archivo2.Damage != "Undamaged" and archivo2.Material == "Glass":
            cpuntos = 1

            caneca = "caneca negra (residuos no aprovechables)"
            enlace_caneca = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"
        usuarios_obj = Usuario.objects.get(nombre=request.user)
        id_archivo1 = request.POST['archivo']
        etiquetas4 = Etiqueta.objects.get(id=id_archivo1)
        id_archivo2 = etiquetas4.id_archivo

        verifier = False
        clasificaciones = Clasificacion.objects.filter(
            Usuario_id_usuario_id=usuarios_obj.id_usuario)
        for e in clasificaciones:
            t = e.id_archivo
            if t == id_archivo2:
                nombre_archivo = []
                verifier = True

        if verifier == False:
            db_clasificacion = Clasificacion(
                id_archivo=id_archivo2, Usuario_id_usuario_id=usuarios_obj.id_usuario)
            db_clasificacion.save()
            db_actividad = Actividad(
                Usuario_id_usuario_id=usuarios_obj.id_usuario, tipo_actividad='clasificado')
            db_actividad.save()
            db_puntos = Puntos(cantidad_puntos=cpuntos,
                               Usuario_id_usuario_id=usuarios_obj.id_usuario)
            db_puntos.save()
            usuarios_obj.total_puntos = usuarios_obj.total_puntos + cpuntos
            usuarios_obj.save()
            nombre_archivo = []
            if cpuntos == 1:
                return render(request, 'clasificado_etiqueta.html', {'etiquetas':etiquetas,'mensaje': "¡Felicitaciones!, ganaste "+str(cpuntos)+" punto.", 'archivo': caneca, 'enlace': enlace_caneca, 'Material': archivo2.Material, 'Package_color': archivo2.Package_color, 'Bottle_cap': archivo2.Bottle_cap, 'Dirtiness': archivo2.Dirtiness, 'Packaging_type': archivo2.Packaging_type, 'Brand': archivo2.Brand, 'Reference': archivo2.Reference, 'Capacity': capacidad, 'Damage': archivo2.Damage})
            else:
                return render(request, 'clasificado_etiqueta.html', {'etiquetas':etiquetas,'mensaje': "¡Felicitaciones!, ganaste "+str(cpuntos)+" puntos.", 'archivo': caneca, 'enlace': enlace_caneca, 'Material': archivo2.Material, 'Package_color': archivo2.Package_color, 'Bottle_cap': archivo2.Bottle_cap, 'Dirtiness': archivo2.Dirtiness, 'Packaging_type': archivo2.Packaging_type, 'Brand': archivo2.Brand, 'Reference': archivo2.Reference, 'Capacity': capacidad, 'Damage': archivo2.Damage})
        else:
            db_clasificacion = Clasificacion(
                id_archivo=id_archivo2, Usuario_id_usuario_id=usuarios_obj.id_usuario)
            db_clasificacion.save()
            db_actividad = Actividad(
                Usuario_id_usuario_id=usuarios_obj.id_usuario, tipo_actividad='clasificado')
            db_actividad.save()
            return render(request, 'clasificado_etiqueta.html', {'etiquetas':etiquetas, 'mensaje': "Como ya habías clasificado este residuo, no ganaste puntos", 'archivo': caneca, 'enlace': enlace_caneca, 'Material': archivo2.Material, 'Package_color': archivo2.Package_color, 'Bottle_cap': archivo2.Bottle_cap, 'Dirtiness': archivo2.Dirtiness, 'Packaging_type': archivo2.Packaging_type, 'Brand': archivo2.Brand, 'Reference': archivo2.Reference, 'Capacity': capacidad, 'Damage': archivo2.Damage})


@login_required(login_url='../login/')
def clasificado_formulario(request):
    try:
        caneca = ""
        enlace_caneca = ""
        material = request.POST['material']
        package_color = request.POST['package_color']
        bottle_cap = request.POST['bottle_cap']
        dirtiness = request.POST['dirtiness']
        packaging_type = request.POST['packaging-type']
        brand = request.POST['brand']
        reference = request.POST['reference']
        capacity = request.POST['capacity']
        damage = request.POST['damage']
        if capacity != "N/A":
            capacidad = capacity + " ml"
        else:
            capacidad = capacity
        if material == "Other plastic":
            caneca = "caneca negra (residuos no aprovechables)"
            enlace_caneca = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"
        elif dirtiness == "Clean" and damage == "Undamaged":
            caneca = "caneca blanca (residuos aprovechables)"
            enlace_caneca = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"
        elif dirtiness != "Clean":
            caneca = "caneca negra (residuos no aprovechables)"
            enlace_caneca = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"
        elif dirtiness == "Clean" and material != "Glass":
            caneca = "caneca blanca (residuos aprovechables)"
            enlace_caneca = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"
        elif damage != "Undamaged" and material == "Glass":
            caneca = "caneca negra (residuos no aprovechables)"
            enlace_caneca = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"
    except:
        archivo = ""
        enlace_caneca = "https://rimoplasticas.com/wp-content/uploads/2020/12/colores-de-la-caneca-de-reciclaje.jpg"
        return render(request, 'clasificado_formulario.html', {'archivo': "...", 'enlace': enlace_caneca})
    else:
        return render(request, 'clasificado_formulario.html', {'archivo': caneca, 'enlace': enlace_caneca, 'Material': material, 'Package_color': package_color, 'Bottle_cap': bottle_cap, 'Dirtiness': dirtiness, 'Packaging_type': packaging_type, 'Brand': brand, 'Reference': reference, 'Capacity': capacidad, 'Damage': damage})


@login_required(login_url='../login/')
def etiquetaExito(request):
    usuarios_obj = Usuario.objects.get(nombre=request.user)
    material = request.POST['material']
    package_color = request.POST['package_color']
    bottle_cap = request.POST['bottle_cap']
    dirtiness = request.POST['dirtiness']
    packaging_type = request.POST['packaging-type']
    brand = request.POST['brand']
    reference = request.POST['reference']
    capacity = request.POST['capacity']
    damage = request.POST['damage']
    id_archivo1 = request.POST['id_archivo']

    pruebaEtiquetas = {
        'Material': material,
        'Package_color': package_color,
        'Bottle_cap': bottle_cap,
        'Dirtiness': dirtiness,
        'Packaging_type': packaging_type,
        'Brand': brand,
        'Reference': reference,
        'Capacity': capacity,
        'Damage': damage
    }

    nombre_archivo = id_archivo1.split()
    id_archivo1 = nombre_archivo[0]


    verifier = False
    etiquetas = Etiqueta.objects.filter(Usuario_id_usuario_id=usuarios_obj.id_usuario)
    for e in etiquetas:
        t = e.id_archivo
        if t == id_archivo1:
            nombre_archivo = []
            verifier = True

    if verifier == False:
        db_etiqueta = Etiqueta(id_archivo=id_archivo1, Usuario_id_usuario_id=usuarios_obj.id_usuario, Material=material, Package_color=package_color,
                               Bottle_cap=bottle_cap, Dirtiness=dirtiness, Packaging_type=packaging_type, Brand=brand, Reference=reference, Capacity=capacity, Damage=damage)
        db_etiqueta.save()
        db_actividad = Actividad(
            Usuario_id_usuario_id=usuarios_obj.id_usuario, tipo_actividad='etiquetado')
        db_actividad.save()
        db_puntos = Puntos(cantidad_puntos=5,
                           Usuario_id_usuario_id=usuarios_obj.id_usuario)
        db_puntos.save()
        usuarios_obj.total_puntos = usuarios_obj.total_puntos + 5
        usuarios_obj.save()
        nombre_archivo = []
        return render(request, 'exito_Etiquetado.html', {'archivo': id_archivo1})
    else:
        db = Etiqueta.objects.filter(Usuario_id_usuario_id = usuarios_obj.id_usuario, id_archivo = id_archivo1)
        db.delete()
        db_etiqueta = Etiqueta(id_archivo=id_archivo1, Usuario_id_usuario_id=usuarios_obj.id_usuario, Material=material, Package_color=package_color,
                               Bottle_cap=bottle_cap, Dirtiness=dirtiness, Packaging_type=packaging_type, Brand=brand, Reference=reference, Capacity=capacity, Damage=damage)
        db_etiqueta.save()
        db_actividad = Actividad(
            Usuario_id_usuario_id=usuarios_obj.id_usuario, tipo_actividad='etiquetado')
        db_actividad.save()
        return render(request, 'exito_Etiquetado2.html', {'archivo': id_archivo1})
