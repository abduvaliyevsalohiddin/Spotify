from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class QoshiqchilarAPi(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        qoshiqchi = request.data
        serializer = QoshiqchiSerializer(data=qoshiqchi)
        if serializer.is_valid():
            data = serializer.validated_data
            Qoshiqchi.objects.create(
                ism=data.get("ism"),
                tugulgan_yil=data.get("tugulgan_yil"),
                davlat=data.get("davlat"),
            )
            return Response(serializer.data)
        return Response(serializer.errors)


class QoshiqlarAPi(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)
