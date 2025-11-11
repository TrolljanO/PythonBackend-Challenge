from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Review(models.Model):
    class Status(models.IntegerChoices):
        """
        dict para definir o status da review
        1 - Publicado
        0 - Rascunho
        """

        DRAFT = (0, "Rascunho")
        PUBLISHED = (1, "Publicado")

    class RatingChoices(models.IntegerChoices):
        """
        dict para definir a avaliação em estrelas
        0 - 0 Estrelas
        1 - 1 Estrela
        2 - 2 Estrelas
        3 - 3 Estrelas
        4 - 4 Estrelas
        5 - 5 Estrelas
        """

        BAD = (0, "Ruim")
        POOR = (1, "Regular")
        FAIR = (2, "Bom")
        GOOD = (3, "Muito Bom")
        EXCELLENT = (4, "Excelente")
        EXCEPTIONAL = (5, "Excepcional")

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    rating = models.IntegerField(
        choices=RatingChoices.choices, default=RatingChoices.GOOD
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.title} - {self.get_status_display()}"  # type: ignore
