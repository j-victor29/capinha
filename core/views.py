from django.shortcuts import render


def home(request):
    """
    Página inicial do projeto.
    Exibe um dashboard com links para os principais apps.
    """
    return render(request, 'home.html', {
        'title': 'Bem-vindo ao Capinha!',
    })
