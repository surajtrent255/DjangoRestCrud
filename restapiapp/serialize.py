from rest_framework import serializers
from .models import *

class EmployeeSerialize(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = "__all__"