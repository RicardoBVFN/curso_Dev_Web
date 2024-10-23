from django.db import models

# Create your models here.

class topic(models.Model):

    """cadastro de um tema que está sendo estudado"""

    texto = models.CharField(max_length=200)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """retorna uma representação em string do modelo"""
        return self.texto

class anotacoes(models.Model):

    """registra uma anotação do tópico"""

    chave = models.ForeignKey(topic, on_delete=models.CASCADE)
    anotacao = models.TextField()
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.anotacao[:50] + '...'

