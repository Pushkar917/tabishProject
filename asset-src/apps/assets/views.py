from sys import implementation
from .models import CryoCart, Implementation_crypto
from .serializers import CryptoCartSerializer, ImplementationCryptoCartSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



class CryoCartList(generics.ListCreateAPIView):
    queryset = CryoCart.objects.all()
    serializer_class = CryptoCartSerializer



class CryoCartListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CryoCart.objects.all()
    serializer_class = CryptoCartSerializer


@api_view([ 'PUT'])
def CryoCartUpdate(request, assetID):
    if request.method == 'PUT':
        cryoCart = CryoCart.objects.get(assetID=assetID) 
        cryoCart_data = JSONParser().parse(request) 
        cryocart_serializer = CryptoCartSerializer(cryoCart, data=cryoCart_data) 
        if cryocart_serializer.is_valid(): 
            cryocart_serializer.save() 
            return JsonResponse(cryocart_serializer.data) 
        return JsonResponse(cryocart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# updating implementation model url or creating implementation model relationship with


class ImplementationCryoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Implementation_crypto.objects.all()
    serializer_class = ImplementationCryptoCartSerializer


class ImplementationCryoRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Implementation_crypto.objects.all()
    serializer_class = ImplementationCryptoCartSerializer





class ImplemetationCryoCartUpdateWithAssetID(APIView):
    
    def get(self, request, assetID):
        implementation = Implementation_crypto.objects.filter(cryocart__assetID=assetID)
        print(implementation)
        serializer = ImplementationCryptoCartSerializer(implementation, many=True)
        print("printing serializer")
        print(serializer)
        return Response(serializer.data)
    
    def put(self, request, assetID):
        implementation = Implementation_crypto.objects.filter(cryocart__assetID=assetID)
        serializer = ImplementationCryptoCartSerializer(implementation, 
                                                  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, assetID):
        implementation = Implementation_crypto.objects.filter(cryocart__assetID=assetID)
        implementation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







