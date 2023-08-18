from django.contrib import admin
from memory.models import modelo_memory_max, modelo_memory_min, modelo_memory_wallet

# Register your models here.
class memory_min(admin.ModelAdmin):
    pass
admin.site.register(modelo_memory_min, memory_min)

# Register your models here.
class memory_max(admin.ModelAdmin):
    pass
admin.site.register(modelo_memory_max, memory_max)

# Register your models here.
class memory_wallet(admin.ModelAdmin):
    pass
admin.site.register(modelo_memory_wallet, memory_wallet)