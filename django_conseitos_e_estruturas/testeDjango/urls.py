from django.urls import path
from testeDjango import views

urlpatterns = [
    path('', views.index, name='topicos'),
    path('teste/', views.cadastro_usario, name='teste')
]