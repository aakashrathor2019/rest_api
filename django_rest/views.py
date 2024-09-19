from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView



                              #*****************Function Based API Views*****************

# Create your views here.
# @api_view(['GET'])
# def studentviewset(request):
#   student_obj=Student.objects.all()
#   serializer=StudentSerializer(student_obj ,many=True)
#   return Response({'status': 200 , 'payload': serializer.data ,'message':'Student Data'})

# @api_view(['POST'])
# def createstudent(request):
#   serializer=StudentSerializer(data=request.data)

#   if not serializer.is_valid():
#     return Response({'status':403,'message':serializer.errors})
  
#   serializer.save()
  
#   return Response({'status': 200 ,'payload':serializer.data , 'message':'New Student Created Successfully '})

# @api_view(['PUT'])
# def updatestudent(request,id):
    
#     try:
#       std_obj=Student.objects.get(st_id=id)
#       serializer=StudentSerializer(std_obj , data=request.data)

#     except:
#       return Response({'status':403,'message':'invalid id !!!'})
    
#     if not serializer.is_valid():
#         return Response({'status':400 ,'message':'Entet data in valid format'})
      
#     serializer.save()
#     return Response({'status':200 ,'message':'data updated successfully'})

# @api_view(['DELETE'])
# def deletestudent(request,id):
#    try:
#       std_obj=Student.objects.get(st_id=id)
#       std_obj.delete()

#    except:
#       return Response({'status':404,'error':'Invalid id!!!'})

#    return Response({'status':200, 'message':'data deleted' })


# @api_view(['GET'])
# def getbook(request):
#     try:
#       book_obj=Book.objects.all()
#       print('Books:',book_obj)
#       serializer=BookSerializer(book_obj, many=True)
#       return Response({'status':200,'payload':serializer.data,'message':'Avaliable Books'})
#     except:
#        return Response({'status':404 ,'message':'There is no book availble'})



                                    #***************Class based API Views*******************
class StudentViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self ,request ,id=None):
      print('ID VAL:',id)
      if id:
         try:
            student_objs=Student.objects.get(st_id=id)
            print('Student Obj:',student_objs)
            serializer=StudentSerializer(student_objs)
            return Response({'status':200,'payload':serializer.data,'message':'Data Found'})
         except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
      else:
        student_objs=Student.objects.all()
        serializer=StudentSerializer(student_objs ,many=True)
        print('Current User:',request.user)
        return Response({'status':200 ,'payload':serializer.data,'message':'All data of student'})

    def post(self ,request):
        serializer=StudentSerializer(data=request.data)

        if  not serializer.is_valid():
            return Response({'status':404,'error':serializer.errors ,'message':'data is not in valid format'})
        
        serializer.save()

        return Response({'status':200,'payload':serializer.data,'message':'New Student created successfully'})
    
    def patch(self,request,id):
      try:
        std_obj=Student.objects.get(st_id=id)
        serializer=StudentSerializer(std_obj,data=request.data,partial=True)

        if not serializer.is_valid():
            return Response({'status':404 ,'error':serializer.errors ,'message':'Invalid Format'})
        
        serializer.save()
        return Response({'status':200 , 'payload':serializer.data ,'message':'data updated sucessfully'})
      except:
          return Response({'status':404 ,'message':'Invalid!!!'})
    
    def put(self,request,id):
      try:
        std_obj=Student.objects.get(st_id=id)
        serializer=StudentSerializer(std_obj,data=request.data )

        if not serializer.is_valid():
            return Response({'status':404 ,'error':serializer.errors ,'message':'Invalid Format'})
        
        serializer.save()
        return Response({'status':200 , 'payload':serializer.data ,'message':'data updated sucessfully'})
      except:
         return Response({'status':404,'messgae':'Invalid!!!'})
    
    def delete(self,request,id):
      try:
        std_obj=Student.objects.get(st_id=id)
        std_obj.delete()
        return Response({'status':200 ,'message':'Data Deleted'})
      
      except:
         return Response({'status':404, 'message':'Id not found'})
      
class ResgisterUser(APIView):
   def post(self, request):
      serializer=UserSerializer(data = request.data)

      if not serializer.is_valid():
         return Response({'status':403 ,'errors':serializer.errors , 'message':'Something went wrong'})
      
      serializer.save()

      user=User.objects.get(username=serializer.data['username'])
      token_obj=Token.objects.get_or_create(user=user)

      return Response({'status':200 ,'payload':serializer.data ,'token':str(token_obj) ,'message':'your data saved'})

 

   
    
  





