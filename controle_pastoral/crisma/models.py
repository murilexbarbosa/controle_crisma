from django.db import models
from crismando.models import Crismando
from catequista.models import Catequista

# Create your models here.
class Turma(models.Model):
    catequista = models.ForeignKey(Catequista, on_delete=models.CASCADE, verbose_name='Catequista')
    crismando = models.ForeignKey(Crismando, on_delete=models.CASCADE, verbose_name='Crismando')


class Encontro(models.Model):
    crismando = models.ForeignKey(Crismando, on_delete=models.CASCADE, verbose_name='Crismando')
    presenca = models.BooleanField(verbose_name='Presença', default=False)
    data_encontro = models.DateField(verbose_name='Data Encontro')
    observacao = models.TextField(verbose_name='Observação', blank=True, null=True)
