from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class QoshiqlarAPi(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)
