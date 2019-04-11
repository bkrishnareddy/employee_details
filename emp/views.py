from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from . models import Employee
from . serializers import EmployeeSerializer

class EmployeeList(APIView):
    def get(self, request):
        print("Checked for Employee")
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self):
        pass
