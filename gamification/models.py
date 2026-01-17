from django.db import models
from users.models import user

class Recompensa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class UsuarioRecompensa(models.Model):
    usuario = models.ForeignKey(user, on_delete=models.CASCADE)
    recompensa = models.ForeignKey(Recompensa, on_delete=models.CASCADE)
    data_recompensa = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'recompensa')
