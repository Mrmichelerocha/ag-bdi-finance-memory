from django.shortcuts import render
from memory.serializer import serializer_max, serializer_min, serializer_wallet
from memory.models import modelo_memory_wallet, modelo_memory_max, modelo_memory_min
from rest_framework import viewsets

# Create your views here.
class min_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_min.objects.all()
    serializer_class = serializer_min
    
class max_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_max.objects.all()
    serializer_class = serializer_max
    
class wallet_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_wallet.objects.all()
    serializer_class = serializer_wallet
    