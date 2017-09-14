from django.contrib import admin

from apps.mascota.models import Marca, Mascota

# Register your models here.
admin.site.register(Marca)
admin.site.register(Mascota)