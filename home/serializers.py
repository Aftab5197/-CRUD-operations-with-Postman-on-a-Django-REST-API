from rest_framework import serializers

from home.models import Employee


class EmployeeSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    email= serializers.EmailField()
    password= serializers.CharField(max_length=100)
    phone= serializers.CharField(max_length=12)
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, employee, validated_data):
        newemployee=Employee(**validated_data)
        newemployee.id=employee.id
        newemployee.save()
        return newemployee
class userSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=100)
    email= serializers.EmailField()
    password= serializers.CharField(max_length=100)
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)

