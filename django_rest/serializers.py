from rest_framework import serializers
from django_rest.models import Student,Book,Category
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):

  class Meta:
     model=Student
     fields='__all__'


  def validate_st_name(self,value):
     
     if any(char.isdigit()  for char in value):
        raise serializers.ValidationError('Name must contaion characters only')
     
     if len(value) < 3:
      print('INSIDE NAME ERROR',len(value))
      raise serializers.ValidationError('Name contains at least 3 characters')
     
     return value
  
  

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta:
      model=Category
      fields='__all__'


class BookSerializer(serializers.ModelSerializer):
   category=CategorySerializer()
   class Meta:
      model=Book
      fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','password']

    def create(self ,validated_data):
       user= User.objects.create(username=validated_data['username'])
       user.set_password(validated_data['password'])
       user.save()
       return user