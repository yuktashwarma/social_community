import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from django_social_comm.Serializers.LikeSerializer import LikeSerializer
from rest_framework.response import Response
from django.core.serializers import serialize
from ..models import LikeStat
from rest_framework import status

class LikeAPIView(APIView):
    curr_state={"state": "none"}
    def update(self, request):
        try:
            response=LikeStat.objects.get(user_id=request.data["user_id"], drama_id=request.data["drama_id"])
            if response is not None and response.drama_id is not None:
                if response.active is True:
                    response.active=False
                    response.last_updated_date=datetime.datetime.now()
                    self.curr_state.update({"state":"False"})
                else:
                    response.active=True
                    response.last_updated_date=datetime.datetime.now()
                    self.curr_state.update({"state":"True"})
                response.save()
                return Response(self.curr_state,content_type="application/json",status=status.HTTP_202_ACCEPTED)
        except:
            like_serializer=LikeSerializer(data=request.data)
            if like_serializer.is_valid():
                like_serializer.save()
                self.curr_state.update({"state":"added new like"})
                return Response(self.curr_state,content_type="application/json",status=status.HTTP_201_CREATED)
            return Response(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        