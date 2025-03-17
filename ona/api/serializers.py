
from rest_framework import serializers
from ona.models import Departs, Employee, EmailTalks


class DepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departs
        fields = '__all__'


class EmployeeDataSerializer(serializers.ModelSerializer):
    depart = DepartsSerializer(read_only=True)  # Dados completos do departamento

    class Meta:
        model = Employee
        fields = '__all__'


class AnalysisDateSerializer(serializers.ModelSerializer):
    data_inicio = serializers.DateField(required=True)
    data_fim = serializers.DateField(required=True)

    class Meta:
        model = EmailTalks
        fields = '__all__'


# class EmailTalksSerializer(serializers.ModelSerializer):
#     destinatario = serializers.StringRelatedField()  # Apenas o nome do destinatário
#     remetente = serializers.StringRelatedField()

#     class Meta:
#         model = EmailTalks
#         fields = ['id', 'remetente', 'destinatario', 'data_envio']