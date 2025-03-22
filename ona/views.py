from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ona.api.serializers import AnalysisDateSerializer, EmailRelationSerializer
from ona.models import EmailTalks, Employee, Departs
from django.db.models import Count, Min
from django.contrib.postgres.aggregates import ArrayAgg
from datetime import datetime, timedelta, date
import hashlib

# Create your views here.

# retorna as interações com o D - 30
class EmailInteractionView(APIView):
    def get(self, request):
        print('entrou no get')
        hoje = date.today()
        interactions = (EmailTalks.objects
                        .filter(data_envio__range=((hoje - timedelta(days=30)), hoje))
                        .values('hash_id')
                        .annotate(total=Count('id'))
                    )
        result = []
        for interaction in interactions:
            emails = EmailTalks.objects.filter(hash_id=interaction['hash_id']).first()
            if emails:
                interaction_data = EmailRelationSerializer(emails).data
                interaction_data['total'] = interaction['total'] # total vem do filter que foi feito no interactions
                result.append(interaction_data)
        return Response(result)
    
# retorna as interações por data definida
class EmailDataView(APIView):
    def post(self, request):
        print('entrou no post')
        serializer = AnalysisDateSerializer(data=request.data)
        if serializer.is_valid():
            data_inicio = serializer.validated_data['data_inicio']
            data_fim = serializer.validated_data['data_fim']
            interactions = (EmailTalks.objects
                            .filter(data_envio__range=(data_inicio, data_fim))
                            .values('hash_id')
                            .annotate(total=Count('id'))
                        )
            result = []
            for interaction in interactions:
                emails = EmailTalks.objects.filter(hash_id=interaction['hash_id']).first()
                if emails:
                    interaction_data = EmailRelationSerializer(emails).data
                    interaction_data['total'] = interaction['total'] # total vem do filter que foi feito no interactions
                    result.append(interaction_data)
            return Response(result)

# retorna as interações entre times com data definida
class TeamInteractionView(APIView):
    def post(self, request):
        serializer = AnalysisDateSerializer(data=request.data)
        if serializer.is_valid():
            data_inicio = serializer.validated_data['data_inicio']
            data_fim = serializer.validated_data['data_fim']
            interactions = (EmailTalks.objects
                            .filter(data_fim, data_inicio)
                            .values('remetente__depart', 'destinatario__depart')
                            .annotate(total=Count('id'))
                            .order_by('-total')
                        )
            result = []
            for interaction in interactions:
                remetente_time = interaction['remetente__depart']
                destinatario_time = interaction['destinatario__depart']

                result.append({
                    'time1': remetente_time,
                    'time_2': destinatario_time,
                    'total_instaracoes': interaction['total']
                })
            return Response(result)

def generate_hash(sender, receiver):
    interaction = f"{min(sender, receiver)}-{max(sender, receiver)}"
    return hashlib.sha256(interaction.encode()).hexdigest()

    
# class EmployeeRelationView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmailRelationSerializer(employees, many=True)
#         return Response(serializer.data)


