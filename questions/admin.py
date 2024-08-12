from django.contrib import admin
from .models import Questao, ImagemEnunciado

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'disciplina', 'gabarito')
    search_fields = ('disciplina', 'gabarito')

@admin.register(ImagemEnunciado)
class ImagemEnunciadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'questao', 'posicao')
    search_fields = ('questao__enunciado',)
