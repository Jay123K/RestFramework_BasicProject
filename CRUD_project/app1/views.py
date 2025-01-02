from django.shortcuts import render
from .Serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def get_Student(request):
    stu=Student.objects.all()
    stuSeri=StudentSerializer(stu,many=True)
    return Response({'status':200,'payload':stuSeri.data})


@api_view(['POST'])
def post_Student(request):
    stuSeri=StudentSerializer(data=request.data)
    if stuSeri.is_valid():
        stuSeri.save()
        return Response({'status':200,'payload':stuSeri.data,'message':'Save data'})
    return Response({'status':403,'payload':stuSeri.errors,'message':'Data incorrect'})



@api_view(['PUT'])
def put_Student(request,id):
    stu=Student.objects.get(id=id)
    stuSeri=StudentSerializer(stu,data=request.data)
    if stuSeri.is_valid():
        stuSeri.save()
        return Response({'status':200,'payload':stuSeri.data,'message':'Save data'})
    return Response({'status':403,'payload':stuSeri.errors,'message':'Data incorrect'})

    
@api_view(['PATCH'])
def patch_Student(request,id):
    stu=Student.objects.get(id=id)
    stuSeri=StudentSerializer(stu,data=request.data,partial=True)
    if stuSeri.is_valid():
        stuSeri.save()
        return Response({'status':200,'payload':stuSeri.data,'message':'Save data'})
    return Response({'status':403,'payload':stuSeri.errors,'message':'Data incorrect'})


@api_view(['DELETE'])
def Del_Student(request,id):
    stu=Student.objects.get(id=id)
    stu.delete()
    return Response({'status':200,'message':'Data  is deleted'})
    

