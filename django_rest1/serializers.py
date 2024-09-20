from rest_framework import serializers
from .models import Student


#Student Serializer
class StudentSerializer(serializers.ModelSerializer):
   
   class Meta:
      model=Student
      fields=['name','roll','city','email']

   def save(self ,**kwargs):
     student=Student(
      name=self.validated_data['name'],
      roll=self.validated_data['roll'],
      city=self.validated_data['city'],
      email=self.validated_data['email']
     )
     student.save()
     return student
