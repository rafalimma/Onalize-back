from django.db import models
# Create your models here.


class Departs(models.Model):
    nome = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nome

class Employee(models.Model):
    nome = models.CharField(max_length=100, default='')
    lider = models.CharField(max_length=100, default='')
    depart = models.ForeignKey(Departs, on_delete=models.CASCADE, null=True, blank=True)
    idade = models.CharField(max_length=10, default='')
    level = models.CharField(max_length=100, default='') # senioridade
    genero = models.CharField(max_length=50, default='')
    raca = models.CharField(max_length=50, default='')
    nacionalidade = models.CharField(max_length=50, default='')
    cidade = models.CharField(max_length=100, default='')
    # cargo
    tipo_colaborador = models.CharField(max_length=50, default='') # tirar 
    salario = models.CharField(max_length=50, default='')
    data_nascimento = models.DateField()
    data_onbording = models.DateField()
    email = models.EmailField(max_length=100, default='')

    def __str__(self):
        return self.nome

class EmailTalks(models.Model):
    tipo = models.CharField(max_length=50, default='') # tirar
    origem = models.CharField(max_length=30, default='') # calendar_api / gmail_api
    hash_id = models.CharField(max_length=200, default='')
    remetente = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emails_enviados') # id do colaborador
    destinatario = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emails_recebidos') # id do colaborador
    data_envio = models.DateTimeField()

