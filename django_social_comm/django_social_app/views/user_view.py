from django.shortcuts import render
from rest_framework.views import APIView
from django_social_comm.Serializers.UserSerializer import UserSerializer
from rest_framework.response import Response
from ..models import User
from rest_framework import status
# Create your views here.
class GetUserAPIView(APIView):
    """This endpoint list all the available todos from the database"""
    def get(self, request, id=None):
        
        if request.GET.get("user_id"):
            user_id=User.objects.filter(user_id=request.GET.get("user_id"))
        else:
            user_id=User.objects.all()
        user_serialiser = UserSerializer(user_id, many=True)
        return Response(user_serialiser.data)

class CreateUserAPIView(APIView):
    def post(self, request):
        user_serializer=UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            create_user_response="successfully added"
            return Response([create_user_response],content_type="application/json",status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)