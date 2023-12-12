from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from .models import *


class QoshiqchiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ism = serializers.CharField()
    tugulgan_yil = serializers.DateField()
    davlat = serializers.CharField()


class AlbomSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'


class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_fayl(self, qiymat):
        if qiymat.url.endswith('.mp3'):
            return qiymat
        raise ValidationError("Fayl .mp3 emas")
