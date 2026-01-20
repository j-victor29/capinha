from django.db import models
from artists.models import Artista


class Colecao(models.Model):
    """
    Coleção de artes de um artista.
    Organiza e agrupa as criações artísticas.
    """
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name='colecoes',
        help_text='Artista criador da coleção'
    )
    nome = models.CharField(
        max_length=150,
        help_text='Nome da coleção'
    )
    descricao = models.TextField(
        blank=True,
        help_text='Descrição da coleção de artes'
    )
    imagem_destaque = models.ImageField(
        upload_to='colecoes/',
        blank=True,
        null=True,
        help_text='Imagem de destaque da coleção'
    )
    ativa = models.BooleanField(
        default=True,
        help_text='Coleção visível e disponível'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'
        ordering = ['-criado_em']
        indexes = [
            models.Index(fields=['artista', 'ativa']),
            models.Index(fields=['-criado_em']),
        ]

    def __str__(self):
        return f'{self.nome} ({self.artista.nome_artistico})'

    @property
    def total_artes(self):
        """Total de artes ativas na coleção."""
        return self.artes.filter(ativa=True).count()


class Arte(models.Model):
    """
    Trabalho artístico criado por um artista.
    É o visual que pode ser aplicado aos produtos.
    """
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name='artes',
        help_text='Artista criador da arte'
    )
    colecao = models.ForeignKey(
        Colecao,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='artes',
        help_text='Coleção a qual a arte pertence (opcional)'
    )
    nome = models.CharField(
        max_length=150,
        help_text='Nome ou título da arte'
    )
    arquivo = models.ImageField(
        upload_to='artes/',
        help_text='Arquivo de imagem da arte (PNG, JPG)'
    )
    descricao = models.TextField(
        blank=True,
        help_text='Descrição ou história da arte'
    )
    ativa = models.BooleanField(
        default=True,
        help_text='Arte disponível para uso'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Arte'
        verbose_name_plural = 'Artes'
        ordering = ['-criado_em']
        indexes = [
            models.Index(fields=['artista', 'ativa']),
            models.Index(fields=['colecao', 'ativa']),
            models.Index(fields=['-criado_em']),
        ]

    def __str__(self):
        return f'{self.nome} - {self.artista.nome_artistico}'

    @property
    def total_personalizacoes(self):
        """Total de personalizações desta arte."""
        return self.personalizacoes.count()


class Personalizacao(models.Model):
    """
    Customização visual aplicada a uma arte.
    Combina: texto, fonte, cor, etc.
    
    É o que será referenciado em um pedido.
    """
    arte = models.ForeignKey(
        Arte,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='personalizacoes',
        help_text='Arte que será personalizada'
    )
    texto = models.CharField(
        max_length=255,
        blank=True,
        help_text='Texto personalizado (nome, frase, número)'
    )
    fonte = models.CharField(
        max_length=100,
        blank=True,
        help_text='Fonte do texto (ex: Arial, Roboto)'
    )
    cor = models.CharField(
        max_length=50,
        blank=True,
        help_text='Cor da personalização (hex, rgb ou nome)'
    )
    preco_extra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text='Preço adicional desta personalização'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Personalização'
        verbose_name_plural = 'Personalizações'
        ordering = ['-criado_em']
        indexes = [
            models.Index(fields=['arte']),
            models.Index(fields=['-criado_em']),
        ]

    def __str__(self):
        partes = []
        if self.texto:
            partes.append(f'Texto: {self.texto[:30]}')
        if self.cor:
            partes.append(f'Cor: {self.cor}')
        return ' | '.join(partes) if partes else f'Personalização #{self.id}'
