from django.db import models

# Create your models here.
class Inicio(models.Model):
    image = models.ImageField(verbose_name='Imagem',upload_to='image', null=True)
    titulo = models.CharField(max_length=150 ,verbose_name='Titulo', null=True, blank=True)
    descricao = models.TextField(verbose_name='Texto', null=True, blank=True)
    link = models.CharField(max_length=150, verbose_name='Link')
    button = models.CharField(max_length=150, verbose_name='Nome do botão')

    def __str__(self):
        return f'{self.titulo}'

class Contato(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome', null=False, blank=False)
    telefone = models.CharField(max_length=150, verbose_name='Telefone', null=False, blank=False)
    email = models.EmailField(verbose_name='Email', null=False, blank=False)

    def __str__(self):
        return f'{self.nome}'