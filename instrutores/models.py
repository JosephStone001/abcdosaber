from django.db import models
from django.urls import reverse
from django.utils import timezone

from titulo.models import Titulo

# Create your models here.
class Instrutores (models.Model):
    """Modelo representando os instrutores"""
    Id = models.AutoField(primary_key=True,
                                 help_text='Identificação do Instrutor')
    rg = models.CharField(max_length=15, null=True,
                                 help_text='Informe a região do instrutor')
    nome = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição do instrutor')
    dataNascimento = models.DateField(null=True, blank=True,
                                    help_text='Informe a Data de Nascimento do Instrutor')
    telefone = models.CharField(max_length=9, null=True,
                                 help_text='Informe telefone de contato dos instrutores')
    ddd = models.CharField(max_length=3, null=True,
                                 help_text='Informe código de área dos instrutores')
    codigo_titulo = models.ForeignKey(Titulo,
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      db_column='titulo_codigo'
                                      )
   
        
    def _str_(self):
        return f'{self.codigo} {self.descricao}'
