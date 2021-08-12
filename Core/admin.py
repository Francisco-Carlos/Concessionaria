from django.contrib import admin
from .models import Marcas,Veiculos,Images
# Register your models here.

class Lista_marcas(admin.ModelAdmin):
    list_display =('id','Marca',)

class Lista_veiculos(admin.ModelAdmin):
    list_display = ('id','Nome','Ano')

class Lista_Imagens(admin.ModelAdmin):
    list_display = ('id','veiculo')
admin.site.register(Marcas,Lista_marcas)
admin.site.register(Veiculos,Lista_veiculos)
admin.site.register(Images,Lista_Imagens)