from django.shortcuts import render
from rest_framework.views import APIView
from django_social_comm.Serializers.LikeSerializer import LikeSerializer
from rest_framework.response import Response
from django.core.serializers import serialize
from ..models import Drama
from rest_framework import status

class LikeAPIView(APIView):