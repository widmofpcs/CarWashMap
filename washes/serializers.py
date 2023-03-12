from rest_framework import serializers

from washes.models import CarWash


class WashesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWash
        fields = '__all__'