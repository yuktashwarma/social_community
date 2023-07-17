from django.shortcuts import render
from rest_framework.views import APIView
from django_social_comm.Serializers.LikeSerializer import LikeSerializer
from rest_framework.response import Response
from django.core.serializers import serialize
from ..models import LikeStat
from rest_framework import status

class LikeAPIView(APIView):
    def get(self, request, id=None):
        if request.GET.get("drama_id"):
            like_id=LikeStat.objects.filter(drama_id=request.GET.get("drama_id"))
        else:
            like_id=LikeStat.objects.filter(active=True).count()
        return Response(like_id)
    

class AddLikeAPIView(APIView):
    curr_state={"state": "none"}
    def post(self, request):
        response=LikeStat.objects.get(user_id=request.data["user_id"])
        if response is not None:
            if response.active is True:
                response.active=False
                self.curr_state.update({"state":"False"})
                validate = serialize('json', self.curr_state)
            else:
                response.active=True
        try:
            response.save()
            return Response(validate,content_type="application/json",status=status.HTTP_201_CREATED)
        except:
            return Response(validate.errors, status=status.HTTP_400_BAD_REQUEST)