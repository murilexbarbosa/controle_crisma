from django.contrib import admin
from .models import Crismando, CrismandoTelefone, CrismandoDocumento

# Register your models here.
class CrismandoAdmin(admin.ModelAdmin):
    pass

class CrismandoTelefoneAdmin(admin.ModelAdmin):
    pass

class CrismandoDocumentoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Crismando)
admin.site.register(CrismandoTelefone)
admin.site.register(CrismandoDocumento)

