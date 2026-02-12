from django.shortcuts import render
from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
	queryset = Employee.objects.all().order_by('id')
	serializer_class = EmployeeSerializer

	def get_queryset(self):
		queryset = super().get_queryset()
		employee_id = self.request.query_params.get('employee_id')
		if employee_id:
			queryset = queryset.filter(pk=employee_id)
		return queryset


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer


def employee_gui(request):
    return render(request, 'employees/gui.html')
