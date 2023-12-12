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


class QoshiqchiAPi(APIView):
    def get(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data)

    def put(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Qoshiqchi.objects.filter(id=pk).update(
                ism=data.get('ism'),
                tugulgan_yil=data.get('tugulgan_yil'),
                davlat=data.get('davlat')
            )
            natija = {
                "xabar": "Tanlangan qo`shiqchi update bo'ldi",
            }
            return Response(natija)
        return Response(serializer.errors)

    def delete(self, request, pk):
        Qoshiqchi.objects.filter(id=pk).delete()
        natija = {
            "xabar": "Tanlangan qochiqchi o'chirildi"
        }
        return Response(natija)


class QoshiqlarAPi(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)
