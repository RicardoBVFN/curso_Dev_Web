from django.shortcuts import render
from .models import pacientes
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def index(request):
    """exibe a página index da aplicação"""

    return render(request, 'testeDjango/index.html')
        
    
def sidePages(request):
    """exibe a side page da aplicação"""  
    return render(request, 'testeDjango/sidePage.html')



def cadastro_usario(request):

    paciente = pacientes()

    paciente.nome_completo = request.POST.get('nome_completo')
    paciente.idade = request.POST.get('idade')
    paciente.sexo = request.POST.get('sexo')
    paciente.curiosidade = request.POST.get('curiosidade')

    paciente.save()


    return HttpResponse('dados cadastrados')

# Create your views here.
