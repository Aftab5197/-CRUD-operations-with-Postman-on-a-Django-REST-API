from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from home.models import Employee
from home.serializers import EmployeeSerializer,userSerializer
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from rest_framework import status


# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method=='GET':
        employees = Employee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=json_data)  # Pass data as a keyword argument
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False )
        else:
            return JsonResponse(serializer.errors,safe=False)

@csrf_exempt
def employeeDetailView(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=204)

    if request.method=='DELETE':
        employee.delete()
        return HttpResponse(status=204)
    elif request.method=='GET':
        serializer=EmployeeSerializer(employee)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='PUT':
        json_data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee,data=json_data)  # Pass data as a keyword argument
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
def userListView(request):
    users=User.objects.all()
    serializer=userSerializer(users,many=True)
    return JsonResponse(serializer.data,safe=False)

