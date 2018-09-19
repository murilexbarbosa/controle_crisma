from django.db import models
from controle_pastoral.crismando.models import Crismando
from controle_pastoral.catequista.models import Catequista

# Create your models here.
class Turma(models.Model):
    catequista = models.ManyToManyField(Catequista,  verbose_name='Catequista')
    crismando = models.ManyToManyField(Crismando,  verbose_name='Crismando')


class Encontro(models.Model):
    crismando = models.ManyToManyField(Crismando,verbose_name='Crismando')
    presenca = models.BooleanField(verbose_name='Presença', default=False)
    data_encontro = models.DateField(verbose_name='Data Encontro')
    observacao = models.TextField(verbose_name='Observação', blank=True, null=True)
