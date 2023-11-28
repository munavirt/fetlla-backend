from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
# Create your views here.

from ..models import Batch,Student
from .serializers import BatchSerializer,StudentSerializer
from .permissions import IsAdminOrReadOnly

from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt



class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListBatchAV(APIView):

    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(
            operation_summary = "For list all Batch Details"
    )
    def get(self,request):
        batch = Batch.objects.all()
        serializer = BatchSerializer(batch,many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
            operation_summary = "For creating Batch Details"
    )
    def post(self,request):
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DetailBatchAV(APIView):

    permission_classes = [IsAdminOrReadOnly]
    @swagger_auto_schema(
            operation_summary = "Retrieve details of a specific Batch."
    )
    def get(request,self,pk):
        try:
            batch = Batch.objects.get(pk=pk)
        except:
            return Response({"Movie Not Found"})
        serializer = BatchSerializer(batch)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
            operation_summary = "Update details of a specific Batch"
    )

    def put(self, request, pk):
        batch = Batch.objects.get(pk=pk)
        serializer = BatchSerializer(batch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    @swagger_auto_schema(
            operation_summary = "Delete a specific Batch"
    )

    def delete(request,self,pk):
        batch = Batch.objects.get(pk=pk)
        batch.delete()
        return Response(status=204)
        
        

class ListStudent(APIView):

    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(
            operation_summary = "For list all Student Details"
    )
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
            operation_summary = "For creating Student Details"
    )
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)


class StudentDetails(APIView):

    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(
            operation_summary = "Retrieve details of a specific Student."
    )
    def get(self,request,pk):
        try:
            student = Student.objects.get(pk=pk)
        except:
            return Response({"Student Not Found"})
        
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    

    @swagger_auto_schema(
            operation_summary = "Update details of a specific Student"
    )
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    @swagger_auto_schema(
            operation_summary = "Delete a specific Student"
    )
    def delete(request,self,pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=204)

