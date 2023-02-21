from rest_framework import serializers

from apps.vakanci.models import (
    Vakanci,
)

class VacanciiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vakanci
        fields=(
            'id', 'job_title', 'selary', 'type', 'description', 'email', 'name',
        )
        read_only_fields=('company',)