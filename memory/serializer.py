from django.urls import path, include
from django.contrib.auth.models import User
from memory.models import modelo_memory_max, modelo_memory_min, modelo_memory_wallet
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
