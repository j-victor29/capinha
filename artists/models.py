from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings

class Artista(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_artista'
    )

    nome_artistico = models.CharField(max_length=150)
    biografia = models.TextField(blank=True)
    instagram = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)

    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_artistico

class ContaBancariaArtista(models.Model):
    artista = models.OneToOneField(
        Artista,
        on_delete=models.CASCADE,
        related_name='conta_bancaria'
    )

    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=20)
    conta = models.CharField(max_length=30)
    tipo_conta = models.CharField(
        max_length=20,
        choices=[
            ('corrente', 'Corrente'),
            ('poupanca', 'Poupança')
        ]
    )

    def __str__(self):
        return f'{self.artista.nome_artistico} - {self.banco}'
