import django_filters
from .models import modelo_memory_wallet

class WalletFilter(django_filters.FilterSet):
    _symbol = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = modelo_memory_wallet
        fields = ['_symbol']
