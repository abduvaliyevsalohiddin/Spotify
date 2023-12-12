from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from .models import *


class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_fayl(self, qiymat):
        if qiymat.url.endswith('.mp3'):
            return qiymat
        raise ValidationError("Fayl .mp3 emas")
