from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer

from .models import Employee

# List all employees or create a new one
# employee/
class EmployeeList(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self):
        pass
'''
def index(request):
    all_employees = Employee.objects.all()
    template = loader.get_template('employee/index.html')
    context = {
        'all_employees': all_employees,
    }
    return HttpResponse(template.render(context, request))


def detail(request, employee_id):
    return HttpResponse("You're looking at employee %s." % employee_id)
'''