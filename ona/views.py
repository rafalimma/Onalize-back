from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ona.api.serializers import AnalysisDateSerializer
from ona.models import EmailTalks
from django.db.models import Count

# Create your views here.

class EmailDataView(APIView):
    def post(self, request):
        print('entrou no post')
        serializer = AnalysisDateSerializer(data=request.data)

        if serializer.is_valid():
            print('entrou aqui')
            data_inicio = serializer.validated_data['data_inicio']
            data_fim = serializer.validated_data['data_fim']

            periodo_analise = (EmailTalks.objects.filter
                               (data_envio__range=(data_inicio, data_fim))
                               .values('hash_id', 'origem', 'remetente', 'destinatario')
                               .annotate(total=Count('id'))
                               )
            print('vai mostrar o período de análise')
            print(periodo_analise)

            return Response(list(periodo_analise))
        print('erro no serializer')
        return Response(serializer.errors)


