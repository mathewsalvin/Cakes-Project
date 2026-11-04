from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cake, Weight,Shape,Category

admin.site.register(Cake)
admin.site.register(Shape)
admin.site.register(Weight)
admin.site.register(Category)