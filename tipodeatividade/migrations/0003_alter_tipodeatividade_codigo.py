# Generated by Django 4.2.18 on 2025-02-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipodeatividade', '0002_alter_tipodeatividade_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodeatividade',
            name='codigo',
            field=models.AutoField(help_text='Código do Tipo de atividade', primary_key=True, serialize=False),
        ),
    ]
