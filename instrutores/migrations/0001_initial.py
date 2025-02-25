# Generated by Django 4.2.18 on 2025-02-11 00:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('titulo', '0003_alter_titulo_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutores',
            fields=[
                ('Id', models.AutoField(help_text='Identificação dos Instrutores', primary_key=True, serialize=False)),
                ('rg', models.CharField(help_text='Informe a região dos instrutores', max_length=15, null=True)),
                ('nome', models.CharField(help_text='Informe a descrição dos instrutores', max_length=70)),
                ('dataNascimento', models.DateField(blank=True, help_text='Informe a Data de Nascimento dos Instrutores', null=True)),
                ('telefone', models.CharField(help_text='Informe telefone de contato dos instrutores', max_length=9, null=True)),
                ('ddd', models.CharField(help_text='Informe código de área dos instrutores', max_length=3, null=True)),
                ('data_registro', models.DateField(default=django.utils.timezone.now, help_text='Informe a data de Registro dos Instrutores')),
                ('codigo_titulo', models.ForeignKey(blank=True, db_column='titulo_codigo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='titulo.titulo')),
            ],
        ),
    ]
