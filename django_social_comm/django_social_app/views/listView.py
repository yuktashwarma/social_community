from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_social_comm.serializers import DataSerializer
from django_social_app.models import User
# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all the available todos from the database"""
    queryset = User.objects.all()
    serializer_class = DataSerializer