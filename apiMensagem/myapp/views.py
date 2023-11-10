from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mensagem
from .serializers import MensagemSerializer

class MensagemListCreateView(APIView):
    def get(self, request, format=None):
        mensagens = Mensagem.objects.all()
        serializer = MensagemSerializer(mensagens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MensagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
