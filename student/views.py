from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .serializer import StudentSerializer   #.serializer is the file name. here serializer.py where StudentSerializer class created 
from .models import Student 
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def add_student(request):
    try:
        params = request.data
        serialised_data = StudentSerializer(data = params)
        if serialised_data.is_valid():
            serialised_data.save()
            return Response({'msg':'student added','status code':201})
        else:
            return Response({'msg':'form not valid','status code':403})
    except:
            return Response({'msg':'something went wrong','status code':500})



@api_view(['GET'])
def view_student(request):
    student_data = Student.objects.all()
    serialised_data = StudentSerializer(student_data,many=True)
    return Response({'students':serialised_data.data}) 



@api_view(['PUT'])
def update_student(request,stdnt_id):
    try:
        params = request.data
        student_dat = Student.objects.get(id = stdnt_id)
        serialised_data = StudentSerializer(student_dat,data=params)
        if serialised_data.is_valid():
            serialised_data.save()
            return Response({'msg':'student updated','status code':201})
        else:
            return Response({'msg':'form not valid','status code':403})
    except:
            return Response({'msg':'student not found','status code':500})
        




@api_view(['DELETE'])
def delete_student(request,stud_id):
    try:
        stud_data = Student.objects.get(id = stud_id)
        stud_data.delete()
        return Response({'msg':'Successfully deleted','status code':202})
    except:
        return Response({'msg':'student not found','status code':404})
    