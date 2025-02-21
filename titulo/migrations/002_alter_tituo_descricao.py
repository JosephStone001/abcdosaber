
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='descricao',
            field=models.CharField(help_text='Informe a descrição do titulo', max_length=100),
        ),
    ]
