from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    telefone = models.CharField(max_length=16, null=True)
    email = models.EmailField(null=True)
    endereco = models.CharField(max_length=150, verbose_name="endereço")
    
    def __str__(self):
        return "Nome: {} | CPF: {}".format(self.nome, self.cpf)

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return "- {} -".format(self.nome)
    
class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    cor = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=50)
    ano = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    
    def __str__(self):
        return "Veículo de placa: {} ".format(self.placa)

class Oleo(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=70, verbose_name="descrição")
    
class Filtro(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=70, verbose_name="descrição")