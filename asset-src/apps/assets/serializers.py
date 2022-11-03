from rest_framework import serializers
from .models import CryoCart, Implementation_crypto, VENDOR_IOQ_PROTOCOL







class ImplementationCryptoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation_crypto
        fields = '__all__'


class VenderIOQProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = VENDOR_IOQ_PROTOCOL
        fields = '__all__'





class CryptoCartSerializer(serializers.ModelSerializer):
    implementation = ImplementationCryptoCartSerializer(many=True, read_only=True)
    vender_protocol = VenderIOQProtocolSerializer(many=True, read_only=True)
    class Meta:
        model = CryoCart
        fields = '__all__'
      




