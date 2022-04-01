from dataclasses import field
from rest_framework import serializers
from .models import pads

class padSerializer(serializers.ModelSerializer):
    class Meta:
        model = pads
        fields = ('pad_id', 'owner', 'active', 'active_since', 'For')