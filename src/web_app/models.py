from django.db import models


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    name = models.CharField(max_length=45, null=False)
    points = models.PositiveIntegerField(default=0)


class Tag(models.Model):
    file_id = models.CharField(max_length=150, null=True, blank=False)
    custom_user_id = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    material = models.CharField(max_length=45, null=True, blank=False)
    package_color = models.CharField(max_length=45, null=True, blank=False)
    bottle_cap = models.CharField(max_length=45, null=True, blank=False)
    dirtiness = models.CharField(max_length=45, null=True, blank=False)
    packaging_type = models.CharField(max_length=45, null=True, blank=False)
    brand = models.CharField(max_length=45, null=True, blank=False)
    reference = models.CharField(max_length=45, null=True, blank=False)
    capacity = models.CharField(max_length=45, null=True, blank=False)
    damage = models.CharField(max_length=45, null=True, blank=False)


class PointsHistory(models.Model):
    custom_user_id = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    custom_user_id = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=45, null=False, blank=False, choices=(('etiquetado', 'etiquetado'), ('clasificado', 'clasificado'), ('canjeo', 'canjeo')))
    date = models.DateTimeField(auto_now_add=True)


class Clasification(models.Model):
    custom_user_id = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=150, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    name = models.CharField(max_length=45, null=False)
    image = models.CharField(max_length=1000, null=False)
    description = models.CharField(max_length=1000, null=False)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
