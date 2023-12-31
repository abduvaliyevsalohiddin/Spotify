from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from .models import *


class QoshiqchiSerializer(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'


class AlbomSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'


class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_fayl(self, qiymat):
        qiymat = str(qiymat)
        if qiymat.endswith('.mp3'):
            return qiymat
        raise ValidationError("Fayl .mp3 emas")

    def validate_davomiylik(self, qiymat):
        if str(qiymat) > "0:07:00":
            raise ValidationError("Qoshiq davomiyligi 00:07:00  dan oshib ketdi !!!")
        return qiymat
