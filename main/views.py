from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Marmalade - Главная',
        'content': "Аромтный кофе и нежнейшие десерты только в Marmalade Coffee!",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Marmalade - О нас',
        'content': "О нас",
        'text_on_page': "Marmalade Coffee — это уютная кофейня, где вы можете насладиться вкусным кофе и разнообразными десертами, такими как макаруны, торты, печенье и мармелад."
    }

    return render(request, 'main/about.html', context)