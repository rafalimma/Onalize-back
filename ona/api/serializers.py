
from rest_framework import serializers
from ona.models import Departs, Employee, EmailTalks
from django.db.models import Count, Min

# trás apenas os employees com departamentos:
class DepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departs
        fields = '__all__'
class EmployeeDataSerializer(serializers.ModelSerializer):
    depart = DepartsSerializer(read_only=True)  # Dados completos do departamento

    class Meta:
        model = Employee
        fields = '__all__'

class EmailRelationSerializer(serializers.ModelSerializer):
    colaborador1 = serializers.PrimaryKeyRelatedField(source='destinatario', read_only=True)
    colaborador2 = serializers.PrimaryKeyRelatedField(source='remetente', read_only=True)

    class Meta:
        model = EmailTalks
        fields = ['hash_id', 'colaborador1', 'colaborador2']

# esse serializer vai estar no reqeust dos times também
class AnalysisDateSerializer(serializers.Serializer):
    data_inicio = serializers.DateField(required=True)
    data_fim = serializers.DateField(required=True)