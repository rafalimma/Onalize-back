
from rest_framework import serializers
from ona.models import Departs, Employee, EmailTalks


class DepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departs
        fields = '__all__'

class EmailTalksSerializer(serializers.ModelSerializer):
    destinatario = serializers.StringRelatedField()  # Apenas o nome do destinatário
    remetente = serializers.StringRelatedField()

    class Meta:
        model = EmailTalks
        fields = ['id', 'remetente', 'destinatario', 'data_envio']


class EmployeeDataSerializer(serializers.ModelSerializer):
    depart = DepartsSerializer(read_only=True)  # Dados completos do departamento
    emails_enviados = EmailTalksSerializer(many=True, read_only=True)  # Todos os e-mails enviados

    class Meta:
        model = Employee
        fields = '__all__'