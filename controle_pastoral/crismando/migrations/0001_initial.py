# Generated by Django 2.0.7 on 2018-09-19 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crismando',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_nascimento', models.DateField(verbose_name='Data Nascimento')),
                ('nome_pai', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do Pai')),
                ('nome_mae', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da Mãe')),
                ('batismo', models.BooleanField(default=True, verbose_name='Batismo')),
                ('eucaristia', models.BooleanField(default=True, verbose_name='Eucaristica')),
                ('ano_crisma', models.CharField(max_length=10, verbose_name='Ano da Crisma')),
            ],
        ),
        migrations.CreateModel(
            name='CrismandoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('R', 'RG'), ('B', 'Certidão de Batismo'), ('M', 'Certidão de Matrimônio'), ('N', 'Certidão de Nascimento'), ('E', 'Certidão de Eucaristia')], max_length=1, verbose_name='Tipo Documento')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='crismandodocumento', verbose_name='Arquivo')),
                ('observacao', models.TextField(verbose_name='Observação')),
                ('crismando', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crismando.Crismando', verbose_name='Crismando')),
            ],
        ),
        migrations.CreateModel(
            name='CrismandoTelefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('R', 'Residencial'), ('C', 'Comercial'), ('E', 'E-mail')], max_length=1, verbose_name='Tipo Telefone')),
                ('descricao', models.CharField(max_length=60)),
                ('crismando', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crismando.Crismando', verbose_name='Crismando')),
            ],
        ),
    ]
