from django.db import models

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=20)  # cliente, artista, admin

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    email_usuario = models.EmailField(unique=True)
    senha_hash = models.CharField(max_length=255)
    status_usuario = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_usuario
    
class UsuarioTelefone(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero_telefone = models.CharField(max_length=20)
    tipo_telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.numero_telefone} - {self.usuario.nome_usuario}"
    
class Recompensa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class UsuarioRecompensa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    recompensa = models.ForeignKey(Recompensa, on_delete=models.CASCADE)
    data_recompensa = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'recompensa')
    
class ContaBancaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=20)
    conta = models.CharField(max_length=20)
    tipo_conta = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.banco} - {self.usuario.nome_usuario}"