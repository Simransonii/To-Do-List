from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import  *

# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=Todoserializer
    
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset=Todo.objects.all()
    serializer_class=Todoserializer
    
class CreateTodo(generics.CreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=Todoserializer

class DeleteTodo(generics.DestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=Todoserializer