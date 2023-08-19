from rest_framework import generics
from django.shortcuts import render
from memory.serializer import serializer_max, serializer_min, serializer_wallet, serializer_transaction
from memory.models import modelo_memory_wallet, modelo_memory_max, modelo_memory_min, modelo_memory_transaction
from rest_framework import viewsets
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import WalletFilter
from .models import modelo_memory_wallet

# Create your views here.
class min_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_min.objects.all()
    serializer_class = serializer_min
    
class max_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_max.objects.all()
    serializer_class = serializer_max
    
class transaction_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_transaction.objects.all()
    serializer_class = serializer_transaction

class wallet_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_wallet.objects.all()
    serializer_class = serializer_wallet
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WalletFilter
