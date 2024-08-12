from django.urls import path
from . import views

urlpatterns = [
    path('lista_questoes/', views.questions_list, name='lista_questoes'),
    path('adicionar/', views.add_question, name='adicionar_questao'),
    path('editar/<int:pk>/', views.edit_question, name='editar_questao'),
    path('excluir/<int:pk>/', views.delete_question, name='excluir_questao'),
    path('gerar_simulados/', views.gerar_simulados, name='gerar_simulados'),
    path('salvar_questao/', views.salvar_questao, name='salvar_questao'),
]
