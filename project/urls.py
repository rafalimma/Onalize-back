"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ona.api import viewsets as employeeviewsets
from ona.views import EmailDataView, EmailInteractionView, TeamInteractionView
from rest_framework import routers

route = routers.DefaultRouter()
# route.register é apenas para viewsets do Django
# cria todas as rotas necessárias GET POST PUT etc
route.register(r'employees', employeeviewsets.EmployeeDataViewSet, basename='Employees')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    # path usado paenas para registrar rotas individuais das views
    path('employeeserelationsbyperiod/', EmailDataView.as_view()),
    path('employeesrelations/', EmailInteractionView.as_view(), name='employeesrelations'),
    path('teamsrelationsbyperiod/', TeamInteractionView.as_view(), name='teamsrelations')
]
