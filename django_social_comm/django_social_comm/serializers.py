from rest_framework import serializers
from django_social_app.models import *

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User, LikeStat, CommentStat, Drama
        fields = "__all__"