# Generated by Django 4.2.18 on 2025-02-12 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='codigo',
            new_name='matricula',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='descricao',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='dataFinal',
            field=models.DateField(default=datetime.datetime(2025, 2, 12, 23, 48, 12, 935703, tzinfo=datetime.timezone.utc), help_text='Informe a Data inicial'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='dataInicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 12, 23, 48, 12, 935703, tzinfo=datetime.timezone.utc), help_text='Informe a Data inicial'),
        ),
    ]
