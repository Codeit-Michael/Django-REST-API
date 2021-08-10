from django.shortcuts import render

# http response for request
from django.http import HttpResponse
# if no object, it throws 404
from django.shortcuts import get_object_or_404
# for returning an API data
from rest_framework.views import APIView
# just like get_object_or_404
from rest_framework.response import Response
# sends back the status like login or not
from rest_framework import status
# importing model so we can modify its data
from .models import employee
# importing our serializer
from .serializers import employeeSerializer

# Create your views here.
class employeelist(APIView):

    # get method - to show the data yo8u already have
    def get(self,request):
        employees = employee.objects.all()
        # 2nd parameter means, it tells we need more than 1 object
        serializer = employeeSerializer(employees, many = True)
        # to return the data
        return Response(serializer.data)

    # post method - helps you to create new data
    def post(self):
        pass