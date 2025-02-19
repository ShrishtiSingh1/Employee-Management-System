from django.shortcuts import render # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .services import EmployeeService
from .serializers import EmployeeSerializer
from django.http import HttpResponse # type: ignore
from .models import Employee

#render html form

def employeeInfo(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employeeInfo.html', {'employees': employees})

#homepage

def home(request):
    return HttpResponse("Welcome to the homepage of the API!")


# employee view

@api_view(['GET'])
def get_employees(request):
    employees = EmployeeService.get_all_employees()  # Get all employees
    serializer = EmployeeSerializer(employees, many=True)  # Serialize employees
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return employees data as response

@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeService.create_employee(request.data)  # Call service to create employee
    if serializer:
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created employee data
    return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)  # Handle invalid data

@api_view(['PUT'])
def update_employee(request, pk):
    serializer = EmployeeService.update_employee(pk, request.data)  # Call service to update employee
    if serializer:
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated employee data
    return Response({"error": "Employee not found or invalid data"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee(request, pk):
    if EmployeeService.delete_employee(pk):  # Call service to delete employee
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)  # Return success message
    return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)  # Handle employee not found

