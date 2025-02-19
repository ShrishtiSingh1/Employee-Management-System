from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeService:
    @staticmethod
    def get_all_employees():
        employees = Employee.objects.all()  
        return employees

    @staticmethod
    def get_employee_by_id(employee_id):
        try:
            return Employee.objects.get(id=employee_id)  
        except Employee.DoesNotExist:
            return None 

    @staticmethod
    def create_employee(data):
        serializer = EmployeeSerializer(data=data)  
        if serializer.is_valid():
            serializer.save()  
            return serializer  
        return None 

    @staticmethod
    def update_employee(employee_id, data):
        employee = EmployeeService.get_employee_by_id(employee_id)  
        if employee:
            serializer = EmployeeSerializer(employee, data=data)  
            if serializer.is_valid():
                serializer.save() 
                return serializer  
        return None  

    @staticmethod
    def delete_employee(employee_id):
        employee = EmployeeService.get_employee_by_id(employee_id)  
        if employee:
            employee.delete()  
            return True 
        return False  # Return False if employee not found
