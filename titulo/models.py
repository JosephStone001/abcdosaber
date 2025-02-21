from django.db import models
from django.urls import reverse

# Create your models here.
class Titulo (models.Model):
    """Modelo representando um titulo"""
    codigo = models.IntegerField(primary_key=True,
                                 help_text='Código do titulo')
    descricao = models.CharField(max_length=100, null=False,
                                 help_text='Informe a descrição do titulo')
    
    def _str_(self):
        return f'{self.codigo} {self.descricao}'


