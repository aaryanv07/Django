from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields=['name','age','city']
        fields='__all__' # to include all the fields
        # exclude=['id'] # to exclude the id field


