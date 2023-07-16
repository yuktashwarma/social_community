from rest_framework import serializers
from django_social_app.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentStat
        fields = "__all__"