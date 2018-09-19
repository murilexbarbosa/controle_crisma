from django.contrib import admin
from .models import Catequista

# Register your models here.

class CatequistaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catequista)