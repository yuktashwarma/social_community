from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_social_comm.serializers import DataSerializer
from rest_framework.response import Response
from ..models import User
# Create your views here.
class GetUserAPIView(ListAPIView):
    """This endpoint list all the available todos from the database"""
    queryset = User.objects.all()
    def get(self, request, id=None):
        
        if request.GET.get("user_id"):
            user_id=User.objects.filter(user_id=request.GET.get("user_id"))
        else:
            user_id=User.objects.all()
        user_serialiser = DataSerializer(user_id, many=True)
        return Response(user_serialiser.data)

