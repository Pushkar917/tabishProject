from .models import CryoCart, Implementation_crypto
from .serializers import CryptoCartSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics



class CryoCartList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        cryocart = CryoCart.objects.all()
        serializer = CryptoCartSerializer(cryocart, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CryptoCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CryoCartListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CryoCart.objects.all()
    serializer_class = CryptoCartSerializer
