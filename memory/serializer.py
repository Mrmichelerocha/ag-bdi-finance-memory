from django.urls import path, include
from django.contrib.auth.models import User
from memory.models import modelo_memory_max, modelo_memory_min, modelo_memory_wallet, modelo_memory_transaction
from rest_framework import serializers

# Serializers define the API representation.
class serializer_min(serializers.ModelSerializer):
    class Meta:
        model = modelo_memory_min
        fields = '__all__'
    
# Serializers define the API representation.
class serializer_max(serializers.ModelSerializer):
    class Meta:
        model = modelo_memory_max
        fields = '__all__'    

# Serializers define the API representation.
class serializer_wallet(serializers.ModelSerializer):
    class Meta:
        model = modelo_memory_wallet
        fields = '__all__'    

# Serializers define the API representation.
class serializer_transaction(serializers.ModelSerializer):
    class Meta:
        model = modelo_memory_transaction
        fields = ('id', '_transaction', '_operation', '_quant', '_price_now', '_price_min', '_price_max', '_date')
