from django.db import models

class Categoria(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete= models.PROTECT)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome