from rest_framework import serializers
from apps.merop.models import (
    Event,
)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'date', 'image', 'name', 'location', 'description',
        )
        read_only_fields = (
                'company',
        )