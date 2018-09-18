from django.db import models

# Create your models here.
class Catequista(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    data_inicio = models.DateField(verbose_name='Data Início')
    status = models.BooleanField(verbose_name='Status')

    def __str__(self):
            return self.nome