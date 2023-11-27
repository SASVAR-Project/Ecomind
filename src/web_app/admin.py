from django.contrib import admin
from web_app.models import CustomUser
from web_app.models import Tag
from web_app.models import PointsHistory
from web_app.models import Activity
from web_app.models import Product

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Tag)
admin.site.register(PointsHistory)
admin.site.register(Activity)
admin.site.register(Product)
