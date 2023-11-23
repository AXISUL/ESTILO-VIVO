from django.db import models
from django.contrib.auth.models import User


class Outfit(models.Model):
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]

    ESTILO_CHOICES = [
        ('Casual', 'Casual'),
        ('Deportivo', 'Deportivo'),
        ('Elegante', 'Elegante'),
        ('Urbano', 'Urbano'),
    ]

    COLOR_CHOICES = [
        ('Negro', 'Negro'),
        ('Blanco', 'Blanco'),
        ('Beige', 'Beige'),
        ('Gris', 'Gris'),
        ('Azul', 'Azul'),
    ]

    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    estilo_prenda = models.CharField(max_length=100, choices=ESTILO_CHOICES)
    color_prenda = models.CharField(max_length=50, choices=COLOR_CHOICES)
    imagen = models.ImageField(upload_to='outfit_images/', null=True)

    comentarios = models.ManyToManyField(User, through='Comentario', related_name='comentarios', blank=True)
    cantidad_corazones = models.PositiveIntegerField(default=0)
    usuarios_que_dieron_corazon = models.ManyToManyField(User, related_name='corazones_dados', blank=True)

    def __str__(self):
        return f'{self.genero} - {self.estilo_prenda} - {self.color_prenda}'

class Comentario(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='comentarios_outfit')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f'Comentario por {self.usuario.username} en {self.outfit}'
