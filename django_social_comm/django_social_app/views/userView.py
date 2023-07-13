from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from django_social_comm.serializers import DataSerializer
from ..models import User

# Create your views here.
class CreateUserAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    def post(self, request):
        queryset = User.objects.all()
        serializer_class = DataSerializer
