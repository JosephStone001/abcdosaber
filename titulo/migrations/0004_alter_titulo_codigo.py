# Generated by Django 4.2.18 on 2025-02-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0003_alter_titulo_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='codigo',
            field=models.AutoField(help_text='Código do titulo', primary_key=True, serialize=False),
        ),
    ]
