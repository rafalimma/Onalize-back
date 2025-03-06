from rest_framework import viewsets
from rest_framework.response import Response
from ona.models import Employee
from ona.api.serializers import EmployeeDataSerializer

# ViewSet personalizado que traz Employees + Emails + Departamentos
class EmployeeDataViewSet(viewsets.ViewSet):
    def list(self, request):
        employees = Employee.objects.prefetch_related('emails_enviados').select_related('depart')
        serializer = EmployeeDataSerializer(employees, many=True)
        return Response(serializer.data)