from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Aluno (models.Model):
    """Modelo representando um aluno"""
    matricula = models.AutoField(primary_key=True,
                                 help_text='Matricula do aluno')
    nome = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição do aluno')
    dataInicial = models.DateField(null=False,
                                   default=timezone.now(),
                                   help_text='Informe a Data inicial')
    
    dataFinal = models.DateField(null=False,
                                 default=timezone.now(),
                                 help_text='Informe a Data inicial')
    
    teste = models.CharField(null=True, blank=True, max_length=100)
        
    def _str_(self):
        return f'{self.matricula} {self.nome}'


