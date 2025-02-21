from django.db import models
from django.urls import reverse
from django.utils import timezone


from tipodeatividade.models import TipoDeAtividade
from aluno.models import Aluno
from instrutores.models import Instrutores


"""Modelo representando um Turmas"""

class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text="Informe a turma do Aluno")
    horario_aula = models.TimeField(help_text="Informe a hora em que a hora da aula da Turma")
    duracao_aula = models.SmallIntegerField(default=30, help_text="Informe a duração da aula da Turma")
    data_inicial = models.DateField(default=timezone.now(), help_text="Informe a data inicial da Turma")    
    data_final = models.DateField(null=True,blank=True, help_text="Informe a data final da Turma")
    codigo_atividade = models.ForeignKey(TipoDeAtividade, on_delete=models.CASCADE)
    matricula_monitor = models.ForeignKey(Aluno, null=True, blank=True, on_delete=models.SET_NULL)
    id_instrutor = models.ForeignKey(Instrutores, null=True, on_delete=models.CASCADE)

    
    class Meta:
        ordering = ['numero']
    
    def str(self):
        return f'Turma: {self.numero} - Instrutor: {self.id_instrutor.nome} - Monitor: {self.matricula_monitor.nome}'


class TurmaAluno(models.Model):
    numero_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, help_text="Turma do aluno.")
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, help_text="Matrícula do aluno.")
    data_inicio_matricula = models.DateField(null=False, default=timezone.now,help_text="Data da matrícula do aluno.")
    data_fim_matricula= models.DateField(null=True, blank=True, help_text="Data fim de matrícula do aluno.")
    
    def __str__(self):
        resposta = f' Turma: {self.id} - Aluno: {self.matricula_aluno} - Matricula: {self.data_inicio_matricula.strftime("%d/%m/%y")}'
        data_fim_matricula = self.data_fim_matricula.strftime("%d/%m/%y") if self.data_fim_matricula else ''
        
        if data_fim_matricula:
            resposta += ' até ' + data_fim_matricula
            
        return resposta
    
class Ausencia(models.Model):
    numero_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, help_text="Turma do aluno.")
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, help_text="Matrícula do aluno.")
    data_ausencia = models.DateField(null=False, 
                                     default=timezone.now(),
                                     help_text="Data da falta do aluno da turma.")
    
    
    def str(self):
        resposta = f' Turma: {self.numero_turma} - Aluno: {self.matricula_aluno} - Ausencia: {self.data_ausencia.strftime("%d/%m/%y")}'
      
        return resposta