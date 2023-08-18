from django.db import models
# Create your models here.

class modelo_memory_min(models.Model):
    _symbol = models.CharField(max_length=100)
    _price_min = models.FloatField()
    
class modelo_memory_max(models.Model):
    _symbol = models.CharField(max_length=100)
    _price_min = models.FloatField()
    
class modelo_memory_wallet(models.Model):
    _symbol = models.CharField(max_length=100)
    _price_min = models.FloatField()
    _price_now = models.FloatField()
    _quant = models.IntegerField()
