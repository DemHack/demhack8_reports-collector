from rest_framework import serializers
from .models import *


class BlockedResourceSerializer(serializers.ModelSerializer):
    calls_number = serializers.IntegerField()

    class Meta:
        model = BlockedResource
        fields = (
            'id',
            'title',
            'url',
            'is_approved',
            'calls_number'
        )


class ReportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportItem
        fields = (
            'id',
            'url',
            'time',
        )
