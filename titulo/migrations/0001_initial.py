
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='titulo',
            fields=[
                ('codigo', models.IntegerField(help_text='titulo', primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Informe a descrição do titulo', max_length=70)),
            ],
        ),
    ]
