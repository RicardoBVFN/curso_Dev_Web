from django.shortcuts import render

def index(request):
    """exibe a página index da aplicação"""

    return render(request, 'testeDjango/index.html')
        
    
def sidePages(request):
    """exibe a side page da aplicação"""  
    return render(request, 'testeDjango/sidePage.html')
# Create your views here.
