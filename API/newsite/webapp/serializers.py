from rest_framework import serializers
from .models import employee

class employeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = employee
		# you can declare here what model attributes you want to return like:
		# fields = ('firstname','lastname')

		# except you to return them all:
		fields = '__all__'