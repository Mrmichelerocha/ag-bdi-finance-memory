from django.db import models
# Create your models here.

class modelo_memory_min(models.Model):
    _symbol = models.CharField(max_length=100)
    _price_min = models.FloatField()
    
    def __str__(self):
        return self._symbol
    
class modelo_memory_max(models.Model):
    _symbol = models.CharField(max_length=100)
    _price_max = models.FloatField()
    
    def __str__(self):
        return self._symbol

class modelo_memory_wallet(models.Model):
    _symbol = models.CharField(max_length=255)
    _quant = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self._symbol

class modelo_memory_transaction(models.Model):
    TYPE_OPERATION = [
        ('BUY', 'buy'),
        ('SELL', 'sell'),
    ]
    _transaction = models.CharField(max_length=100)
    _operation = models.CharField(max_length=10, choices=TYPE_OPERATION)
    _quant = models.PositiveIntegerField()
    _price_now = models.FloatField()
    _price_min = models.FloatField()
    _price_max = models.FloatField()
    _date = models.DateTimeField(auto_now_add=True)
    _wallet = models.ForeignKey(modelo_memory_wallet, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        # Obtenha ou crie um modelo_memory_wallet baseado no _transaction
        wallet, created = modelo_memory_wallet.objects.get_or_create(_symbol=self._transaction)

        # Se a operação for compra, adicione a quantidade à carteira
        if self._operation == 'BUY':
            wallet._quant += self._quant

        # Se a operação for venda, subtraia da carteira (verifique se há quantidade suficiente primeiro)
        elif self._operation == 'SELL':
            if wallet._quant < self._quant:
                raise ValueError("Não há itens suficientes na carteira para vender")
            wallet._quant -= self._quant
        
        # Salve as alterações na carteira
        wallet.save()

        # Atribua esta carteira à transação atual
        self._wallet = wallet

        # Chame o método save() da classe base para completar a operação
        super(modelo_memory_transaction, self).save(*args, **kwargs)
