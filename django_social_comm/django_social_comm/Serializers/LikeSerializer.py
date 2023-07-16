from rest_framework import serializers
from django_social_app.models import *

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeStat
        fields = "__all__"