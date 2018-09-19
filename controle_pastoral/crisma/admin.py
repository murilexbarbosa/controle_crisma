from django.contrib import admin
from .models import Turma, Encontro

# Register your models here.
class TurmaAdmin(admin.ModelAdmin):
    pass

class EncontroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Turma)
admin.site.register(Encontro)
