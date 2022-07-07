from django.shortcuts import render

from .models import Inicio, Contato

# Create your views here.
def index(request):

    inicios = Inicio.objects.last()

    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']

        contato = Contato(nome=nome, telefone=telefone, email=email)
        contato.save()

    context = {
        'inicios': inicios
    }

    return render(request, 'index.html', context)


