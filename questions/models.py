from django.db import models

class Questao(models.Model):
    enunciado = models.TextField()
    disciplina = models.CharField(max_length=255)
    gabarito = models.CharField(max_length=10)

    def __str__(self):
        return f"Questão {self.id}"

class ImagemEnunciado(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name="imagens_enunciado")
    imagem = models.ImageField(upload_to="imagens_enunciado/")
    posicao = models.PositiveIntegerField(default=0)  # Posição da imagem no enunciado

    def __str__(self):
        return f"Imagem {self.id} - Questão {self.questao.id}"
