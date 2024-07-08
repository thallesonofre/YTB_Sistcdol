from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    telefone = models.CharField(max_length=16, null=True)
    email = models.EmailField(null=True)
    endereco = models.CharField(max_length=150, verbose_name="endereço")
    
class Marca(models.Model):
    nome = models.CharField(max_length=50)
    
class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    cor = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=50)
    ano = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    
class Oleo(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=70, verbose_name="descrição")
    
class Filtro(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=70, verbose_name="descrição")