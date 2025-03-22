from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ona.api.serializers import AnalysisDateSerializer, EmailRelationSerializer
from ona.models import EmailTalks, Employee, Departs
from django.db.models import Count, Min
from django.contrib.postgres.aggregates import ArrayAgg
from datetime import datetime, timedelta, date

# Create your views here.

class EmailInteractionView(APIView):
    def get(self, request):
        print('entrou no get')
        hoje = date.today()
        interactions = (EmailTalks.objects
                        .filter(data_envio__range=('2024-01-01', '2025-03-18'))
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
    
class EmployeeRelationView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmailRelationSerializer(employees, many=True)
        return Response(serializer.data)


