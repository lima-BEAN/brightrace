from django.shortcuts import render
from employee.models import Employee
from rest_framework import viewsets
from rest_framework import permissions
from employee.serializers import EmployeeSerializer



# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('department')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
