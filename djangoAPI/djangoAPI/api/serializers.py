from django.contrib.auth.models import Snippet
from rest_framework import serializers


class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('url')


class IPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('urls')