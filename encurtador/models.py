from django.db import models
from .utils import criar_shortcode

# Create your models here.

class URL(models.Model):
    # cria campo url, do tipo CharField, tamanho máximo 220:
    url = models.CharField(max_length=220)
    # cria campo shortcode, tamanho máximo 15
    shortcode = models.CharField(max_length=15, null=True,
                                 blank=True, unique=True,
                                 # default="codigopadrao",
                                 )
    # campos autopreenchidos p/ data de atualização e criação
    atualizado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # testa se o shortcode é nulo ou está em branco
        # mesmo que: if self.shortcode in (None,""):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = criar_shortcode(self)
        super(URL, self).save(*args, **kwargs)
    

    # método que retorna string com identificação do objeto
    def __str__(self):
        return str(self.url)  # retorna a url
        # return str(self.pk)  # retorna a chave primária
        # return str(self.shortcode)  # retorna o shortcode
