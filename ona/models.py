from django.db import models
# Create your models here.


class Departs(models.Model):
    # id
    nome = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nome

class Employee(models.Model):
    # id
    nome = models.CharField(max_length=100, default='')
    depart = models.ForeignKey(Departs, on_delete=models.CASCADE, null=True, blank=True)
    idade = models.CharField(max_length=10, default='')
    level = models.CharField(max_length=100, default='')
    genero = models.CharField(max_length=50, default='')
    departamento = models.CharField(max_length=100, default='')
    raca = models.CharField(max_length=50, default='')
    nacionalidade = models.CharField(max_length=50, default='')
    cidade = models.CharField(max_length=100, default='')
    tipo_colaborador = models.CharField(max_length=50, default='')
    salario = models.CharField(max_length=50, default='')
    data_nascimento = models.DateField()
    data_onbording = models.DateField()

    def __str__(self):
        return self.nome

class EmailTalks(models.Model):
    # id
    remetente = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emails_enviados')
    destinatario = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emails_recebidos')
    data_envio = models.DateTimeField()

