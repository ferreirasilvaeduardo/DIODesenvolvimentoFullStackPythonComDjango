import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("Texto da Questão", max_length=200)
    pub_date = models.DateTimeField("Data de Publicação")
    active = models.BooleanField("Ativo", default=True)
    # x = models.TextField(default="Teste")

    class Meta:
        verbose_name_plural = "Questões"
        verbose_name = "Questão"

    def __str__(self) -> str:
        return self.question_text

    # ...
    # NOTE: Esta função depende da biblioteca externa "polls"
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Questão"
    )
    choice_text = models.CharField("Descrição", max_length=200)
    votes = models.IntegerField("Votos", default=0)

    class Meta:
        verbose_name_plural = "Opções"
        verbose_name = "Opção"

    def __str__(self) -> str:
        return self.choice_text
