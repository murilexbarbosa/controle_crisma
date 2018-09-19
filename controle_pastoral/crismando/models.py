from django.db import models

# Create your models here.
class Crismando(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    nome_pai = models.CharField(max_length=100,blank=True, null=True, verbose_name='Nome do Pai')
    nome_mae = models.CharField(max_length=100,blank=True, null=True, verbose_name='Nome da Mãe')
    batismo = models.BooleanField(default=True, verbose_name='Batismo')
    eucaristia = models.BooleanField(default=True, verbose_name='Eucaristica')
    ano_crisma = models.CharField(max_length=10, verbose_name='Ano da Crisma')

    def __str__(self):
            return self.nome


class CrismandoTelefone(models.Model):
    TIPO_CHOICES = (
        ('R', 'Residencial'),
        ('C', 'Comercial'),
        ('E', 'E-mail'),
    )
    crismando = models.ForeignKey(Crismando, on_delete=models.CASCADE, verbose_name='Crismando')
    tipo = models.CharField(max_length=1, verbose_name='Tipo Telefone', choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=60)
    

class CrismandoDocumento(models.Model):
    TIPO_CHOICES = (
        ('R', 'RG'),
        ('B', 'Certidão de Batismo'),
        ('M', 'Certidão de Matrimônio'),
        ('N', 'Certidão de Nascimento'),
        ('E', 'Certidão de Eucaristia'),
    )
    crismando = models.ForeignKey(Crismando,on_delete=models.CASCADE,verbose_name='Crismando')
    tipo = models.CharField(max_length=1, verbose_name='Tipo Documento', choices=TIPO_CHOICES )
    arquivo = models.FileField(upload_to='crismandodocumento', verbose_name='Arquivo', blank=True, null=True)
    observacao = models.TextField(verbose_name='Observação')

