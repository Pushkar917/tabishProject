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


class ImplementationNestedSerializer(serializers.ModelSerializer):
    cryocart = CryptoCartSerializer(many=True, required=False)
    cryo_cart = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Implementation_crypto
        fields = '__all__'

