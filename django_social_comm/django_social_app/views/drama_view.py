from django.shortcuts import render
from rest_framework.views import APIView
from django_social_comm.Serializers.DramaSerializer import DramaSerializer
from rest_framework.response import Response
from django.core.serializers import serialize
from ..models import Drama
from rest_framework import status
# Create your views here.
class GetDramaAPIView(APIView):
    """This endpoint list all the available todos from the database"""
    def get(self, request, id=None):
        
        if request.GET.get("drama_id"):
            drama_id=Drama.objects.filter(drama_id=request.GET.get("drama_id"))
        else:
            drama_id=Drama.objects.all()
        drama_serialiser = DramaSerializer(drama_id, many=True)
        return Response(drama_serialiser.data)

class CreateDramaAPIView(APIView):
    def post(self, request):
        drama_serializer=DramaSerializer(data=request.data)
        if drama_serializer.is_valid():
            drama_serializer.save()
            create_drama_response="successfully added"
            return Response([create_drama_response],content_type="application/json",status=status.HTTP_201_CREATED)
        return Response(drama_serializer.errors, status=status.HTTP_400_BAD_REQUEST)