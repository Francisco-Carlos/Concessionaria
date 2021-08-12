from django.db import models

# Create your models here.
class Marcas(models.Model):
    Marca = models.CharField(max_length=200)

    def __str__(self):
        return self.Marca


class Veiculos(models.Model):
    Nome = models.CharField(max_length=200)
    Marca = models.ForeignKey(Marcas,on_delete=models.CASCADE)
    Preco = models.DecimalField(max_digits=9,decimal_places=2)
    Imagem = models.ImageField(upload_to="veiculosImg/%d/%m%Y")
    Ano   = models.IntegerField()

    def __str__(self):
        return self.Nome


class Images(models.Model):
    veiculo = models.ForeignKey(Veiculos,on_delete=models.CASCADE)
    imagens = models.ImageField(upload_to="veiculosImg/%d/%m%Y")