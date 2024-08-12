from django import forms
from .models import Questao, ImagemEnunciado

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ['enunciado', 'disciplina', 'gabarito']

class ImagemEnunciadoForm(forms.ModelForm):
    class Meta:
        model = ImagemEnunciado
        fields = ['imagem', 'posicao']
