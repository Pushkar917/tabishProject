from rest_framework import serializers
from .models import CryoCart, Implementation_crypto



class CryptoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryoCart
        fields = '__all__'



class ImplementationCryptoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation_crypto
        fields = '__all__'


