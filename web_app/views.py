
from django.shortcuts import render
from web_app.models import CustomUser
from web_app.models import Tag
from web_app.models import PointsHistory
from web_app.models import Activity
from web_app.models import Product
from web_app.models import Clasification

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

id2 = 1


def credits(request):
    return render(request, 'credits.html')


def register(request):
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
                customUser = CustomUser(name=user)
                customUser.save()
                user2 = authenticate(request, username=user, password=pwd)
                login(request, user2)
                return redirect('../home/')

        context = {'form': form}
        return render(request, 'register.html', context)


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
    user_obj = CustomUser.objects.get(name=request.user)
    return render(request, 'home.html', {'name': user_obj.name})


@login_required(login_url='../login/')
def my_points(request):
    user_obj = CustomUser.objects.get(name=request.user)
    pointsHistory = PointsHistory.objects.filter(custom_user_id=user_obj)
    return render(request, 'my_points.html', {'pointsHistory': pointsHistory, 'points': user_obj.points, 'name': user_obj.name})


@login_required(login_url='../login/')
def store(request):
    products = Product.objects.all()
    user_obj = CustomUser.objects.get(name=request.user)
    pointsHistory = PointsHistory.objects.filter(custom_user_id=user_obj.id)
    try:
        prod = request.POST['producto_elegido']
    except:
        if pointsHistory == 1:
            return render(request, 'store.html', {'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " punto", 'name': user_obj.name})
        else:
            return render(request, 'store.html', {'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " puntos", 'name': user_obj.name})
    else:
        product = Product.objects.get(id=prod)
        if product.stock > 0 and user_obj.points >= product.price:
            user_obj.points = user_obj.points - product.price
            user_obj.save()
            product.stock = product.stock - 1
            product.save()
            activity = Activity(custom_user_id=user_obj, type='canjeo')
            activity.save()
            pointsHistory2 = PointsHistory(points=int("-" + str(product.price)), custom_user_id=user_obj)
            pointsHistory2.save()
            message = "¡Has adquirido satisfactoriamente tu incentivo!"
            if pointsHistory == 1:
                return render(request, 'store.html', {'message': message, 'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " punto", 'name': user_obj.name})
            else:
                return render(request, 'store.html', {'message': message, 'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " puntos", 'name': user_obj.name})
        elif product.stock == 0:
            message = "Lo sentimos, no hay existencias disponibles del producto que seleccionaste."
            if pointsHistory == 1:
                return render(request, 'store.html', {'message': message, 'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " punto", 'name': user_obj.name})
            else:
                return render(request, 'store.html', {'message': message, 'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " puntos", 'name': user_obj.name})
        elif user_obj.points < product.price:
            lackPoints = product.price - user_obj.points
            if lackPoints == 1:
                message = "Lo sentimos, no tienes puntos suficientes. Te falta " + str(lackPoints) + " punto."
            else:
                message = "Lo sentimos, no tienes puntos suficientes. Te faltan " + str(lackPoints) + " puntos."
            if pointsHistory == 1:
                return render(request, 'store.html', {'message': message, 'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " punto", 'name': user_obj.name})
            else:
                return render(request, 'store.html', {'message': message, 'products': products, 'pointsHistory': pointsHistory, 'points': str(user_obj.points) + " puntos", 'name': user_obj.name})


@login_required(login_url='../login/')
def my_activity(request):
    user_obj = CustomUser.objects.get(name=request.user)
    activities = Activity.objects.filter(custom_user_id=user_obj)
    return render(request, 'my_activity.html', {'activities': activities, 'name': user_obj.name})


@login_required(login_url='../login/')
def tagging(request):
    return render(request, 'tagging.html')


@login_required(login_url='../login/')
def create_tag(request):
    return render(request, 'create_tag.html')


@login_required(login_url='../login/')
def clasify(request):
    return render(request, 'clasify.html')


@login_required(login_url='../login/')
def clasify_by_tag(request):
    user_obj = CustomUser.objects.get(name=request.user)
    tags = Tag.objects.filter(custom_user_id=user_obj)

    try:
        file = request.POST['archivo']
    except:
        file = 0
        can_link = "https://rimoplasticas.com/wp-content/uploads/2020/12/colores-de-la-caneca-de-reciclaje.jpg"
        return render(request, 'clasify_by_tag.html', {'file': "...", 'link': can_link, 'tags': tags})
    else:
        can = ""
        cpoints = 0
        can_link = ""

        file2 = Tag.objects.get(file_id=file, custom_user_id=user_obj)

        if file2.capacity != "N/A":
            capacity = file2.capacity + " ml"
        else:
            capacity = file2.capacity
        if file2.material == "Other plastic":
            can = "caneca negra (residuos no aprovechables)"
            can_link = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"

            cpoints = 1

        elif file2.dirtiness == "Clean" and file2.damage == "Undamaged":
            if file2.material == 'PET':
                cpoints = 2
            elif file2.material == 'PE-HD':
                cpoints = 6
            elif file2.material == 'PVC':
                cpoints = 7
            elif file2.material == 'PE-LD':
                cpoints = 4
            elif file2.material == 'PP':
                cpoints = 2
            elif file2.material == 'PS':
                cpoints = 2
            elif file2.material == 'Other plastic':
                cpoints = 1
            elif file2.material == 'Glass':
                cpoints = 2
            elif file2.material == 'Aluminium':
                cpoints = 17
            elif file2.material == 'Other metal':
                cpoints = 1
            elif file2.material == 'Cardboard':
                cpoints = 2
            elif file2.material == 'Paper print':
                cpoints = 1
            elif file2.material == 'Newspaper':
                cpoints = 2
            elif file2.material == 'Magazine':
                cpoints = 2
            elif file2.material == 'Tetrapack':
                cpoints = 2
            elif file2.material == 'Other':
                cpoints = 1

            can = "caneca blanca (residuos aprovechables)"
            can_link = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"

        elif file2.dirtiness != "Clean":
            cpoints = 1

            can = "caneca negra (residuos no aprovechables)"
            can_link = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"

        elif file2.dirtiness == "Clean" and file2.material != "Glass":

            if file2.material == 'PET':
                cpoints = 2
            elif file2.material == 'PE-HD':
                cpoints = 6
            elif file2.material == 'PVC':
                cpoints = 7
            elif file2.material == 'PE-LD':
                cpoints = 4
            elif file2.material == 'PP':
                cpoints = 2
            elif file2.material == 'PS':
                cpoints = 2
            elif file2.material == 'Other plastic':
                cpoints = 1
            elif file2.material == 'Aluminium':
                cpoints = 17
            elif file2.material == 'Other metal':
                cpoints = 1
            elif file2.material == 'Cardboard':
                cpoints = 2
            elif file2.material == 'Paper print':
                cpoints = 1
            elif file2.material == 'Newspaper':
                cpoints = 2
            elif file2.material == 'Magazine':
                cpoints = 2
            elif file2.material == 'Tetrapack':
                cpoints = 2
            elif file2.material == 'Other':
                cpoints = 1

            can = "caneca blanca (residuos aprovechables)"
            can_link = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"

        elif file2.damage != "Undamaged" and file2.material == "Glass":
            cpoints = 1

            can = "caneca negra (residuos no aprovechables)"
            can_link = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"

        user_obj = CustomUser.objects.get(name=request.user)
        file_id1 = request.POST['archivo']
        tags4 = Tag.objects.get(file_id=file_id1, custom_user_id=user_obj)
        file_id2 = tags4.file_id

        verifier = False
        clasifications = Clasification.objects.filter(custom_user_id=user_obj)
        for e in clasifications:
            t = e.file_id
            if t == file_id2:
                verifier = True

        if verifier is False:
            db_clasification = Clasification(file_id=file_id2, custom_user_id=user_obj)
            db_clasification.save()
            db_activity = Activity(custom_user_id=user_obj, type='clasificado')
            db_activity.save()
            db_points = PointsHistory(points=cpoints, custom_user_id=user_obj)
            db_points.save()
            user_obj.points = user_obj.points + cpoints
            user_obj.save()
            if cpoints == 1:
                return render(request, 'clasify_by_tag.html', {'tags': tags, 'message': "¡Felicitaciones!, ganaste " + str(cpoints) + " punto.", 'file': can, 'link': can_link, 'Material': file2.material, 'Package_color': file2.package_color, 'Bottle_cap': file2.bottle_cap, 'Dirtiness': file2.dirtiness, 'Packaging_type': file2.packaging_type, 'Brand': file2.brand, 'Reference': file2.reference, 'Capacity': capacity, 'Damage': file2.damage})
            else:
                return render(request, 'clasify_by_tag.html', {'tags': tags, 'message': "¡Felicitaciones!, ganaste " + str(cpoints) + " puntos.", 'file': can, 'link': can_link, 'Material': file2.material, 'Package_color': file2.package_color, 'Bottle_cap': file2.bottle_cap, 'Dirtiness': file2.dirtiness, 'Packaging_type': file2.packaging_type, 'Brand': file2.brand, 'Reference': file2.reference, 'Capacity': capacity, 'Damage': file2.damage})
        else:
            db_clasification = Clasification(file_id=file_id2, custom_user_id=user_obj)
            db_clasification.save()
            db_activity = Activity(custom_user_id=user_obj, type='clasificado')
            db_activity.save()
            return render(request, 'clasify_by_tag.html', {'tags': tags, 'message': "Como ya habías clasificado este residuo, no ganaste puntos", 'file': can, 'link': can_link, 'Material': file2.material, 'Package_color': file2.package_color, 'Bottle_cap': file2.bottle_cap, 'Dirtiness': file2.dirtiness, 'Packaging_type': file2.packaging_type, 'Brand': file2.brand, 'Reference': file2.reference, 'Capacity': capacity, 'Damage': file2.damage})


@login_required(login_url='../login/')
def clasify_by_form(request):
    try:
        can = ""
        can_link = ""
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
            capacity = capacity + " ml"
        else:
            capacity = capacity
        if material == "Other plastic":
            can = "caneca negra (residuos no aprovechables)"
            can_link = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"
        elif dirtiness == "Clean" and damage == "Undamaged":
            can = "caneca blanca (residuos aprovechables)"
            can_link = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"
        elif dirtiness != "Clean":
            can = "caneca negra (residuos no aprovechables)"
            can_link = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"
        elif dirtiness == "Clean" and material != "Glass":
            can = "caneca blanca (residuos aprovechables)"
            can_link = "https://i.postimg.cc/vBC5gj0Y/7ec7efb0-caneca-blanca-para-separacion-de-residuos-y-reciclaje-150x150-1.png"
        elif damage != "Undamaged" and material == "Glass":
            can = "caneca negra (residuos no aprovechables)"
            can_link = "https://i.postimg.cc/gjM4T4D1/137d264c-caneca-negra-para-separacion-de-residuos-y-reciclaje.png"
    except:
        can_link = "https://rimoplasticas.com/wp-content/uploads/2020/12/colores-de-la-caneca-de-reciclaje.jpg"
        return render(request, 'clasify_by_form.html', {'file': "...", 'link': can_link})
    else:
        return render(request, 'clasify_by_form.html', {'file': can, 'link': can_link, 'Material': material, 'Package_color': package_color, 'Bottle_cap': bottle_cap, 'Dirtiness': dirtiness, 'Packaging_type': packaging_type, 'Brand': brand, 'Reference': reference, 'Capacity': capacity, 'Damage': damage})


@login_required(login_url='../login/')
def save_tag(request):
    user_obj = CustomUser.objects.get(name=request.user)
    material = request.POST['material']
    package_color = request.POST['package_color']
    bottle_cap = request.POST['bottle_cap']
    dirtiness = request.POST['dirtiness']
    packaging_type = request.POST['packaging-type']
    brand = request.POST['brand']
    reference = request.POST['reference']
    capacity = request.POST['capacity']
    damage = request.POST['damage']
    file_id1 = request.POST['id_archivo']

    file_name = file_id1.split()
    file_id1 = file_name[0]

    verifier = False
    tags = Tag.objects.filter(custom_user_id=user_obj)
    for e in tags:
        t = e.file_id
        if t == file_id1:
            file_name = []
            verifier = True

    if verifier is False:
        db_tag = Tag(file_id=file_id1, custom_user_id=user_obj, material=material, package_color=package_color,
                     bottle_cap=bottle_cap, dirtiness=dirtiness, packaging_type=packaging_type, brand=brand, reference=reference, capacity=capacity, damage=damage)
        db_tag.save()
        db_activity = Activity(custom_user_id=user_obj, type='etiquetado')
        db_activity.save()
        db_points_history = PointsHistory(points=5, custom_user_id=user_obj)
        db_points_history.save()
        user_obj.points = user_obj.points + 5
        user_obj.save()
        file_name = []
        return render(request, 'save_tag.html', {'file_id': file_id1})
    else:
        db_old_tag = Tag.objects.filter(custom_user_id=user_obj, file_id=file_id1)
        db_old_tag.delete()
        db_tag = Tag(file_id=file_id1, custom_user_id=user_obj, material=material, package_color=package_color,
                     bottle_cap=bottle_cap, dirtiness=dirtiness, packaging_type=packaging_type, brand=brand, reference=reference, capacity=capacity, damage=damage)
        db_tag.save()
        db_activity = Activity(custom_user_id=user_obj, type='etiquetado')
        db_activity.save()
        return render(request, 'save_tag2.html', {'file_id': file_id1})
