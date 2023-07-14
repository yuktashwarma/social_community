from rest_framework import serializers
from django_social_app.models import *

class DramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drama
        fields = "__all__"