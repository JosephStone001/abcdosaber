# Generated by Django 4.2.18 on 2025-02-14 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0005_alter_aluno_datafinal_alter_aluno_datainicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='dataFinal',
            field=models.DateField(default=datetime.datetime(2025, 2, 14, 23, 59, 22, 357123, tzinfo=datetime.timezone.utc), help_text='Informe a Data inicial'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='dataInicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 14, 23, 59, 22, 357123, tzinfo=datetime.timezone.utc), help_text='Informe a Data inicial'),
        ),
    ]
