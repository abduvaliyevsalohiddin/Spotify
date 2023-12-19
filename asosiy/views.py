from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.pagination import PageNumberPagination
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


class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'nom']  # /?search = ....
    ordering_fields = ['sana']  # /?ordering= ....

    @action(detail=True)
    def qoshiq(self, request, pk):
        albom = self.get_object()
        albom_qoshiq = albom.qoshiq_set.all()
        serializer = QoshiqSerializer(albom_qoshiq, many=True)
        return Response(serializer.data)


class QoshiqchiModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'ism', 'davlat']  # /?search = ....
    ordering_fields = ['tugulgan_yil']  # /?ordering= ....
    pagination_class = PageNumberPagination
    pagination_class.page_size = 3

    def get_queryset(self):
        qoshiqchilar = self.queryset
        qidiruv = self.request.query_params.get("qidiruv")  # /?qidiruv
        if qidiruv:
            qoshiqchilar = Qoshiqchi.objects.annotate(
                oxshashlik=TrigramSimilarity("ism", qidiruv)
            ).filter(oxshashlik__gt=0.5).order_by("-oxshashlik")
        return qoshiqchilar

    @action(detail=True)
    def albom(self, request, pk):
        qoshiqchi = self.get_object()
        qoshiqchi_albom = qoshiqchi.albom_set.all()
        serializer = AlbomSerializer(qoshiqchi_albom, many=True)
        return Response(serializer.data)


class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'nom', 'janr']  # /?search = ....
    ordering_fields = ['davomiylik']  # /?ordering= ....
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 2

    def get_queryset(self):
        qoshiqlar = self.queryset
        qidiruv = self.request.query_params.get("qidiruv")  # /?qidiruv
        if qidiruv:
            qoshiqlar = Qoshiq.objects.annotate(
                oxshashlik=TrigramSimilarity("nom", qidiruv)
            ).filter(oxshashlik__gt=0.5).order_by("-oxshashlik")
        return qoshiqlar
