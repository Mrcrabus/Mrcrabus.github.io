from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'title': 'Наша первая запись',
        'text': 'Просто большой текст',
        'date': '1.01.2019',
        'author': 'Geog'
    },
    {
        'title': 'Наша вторая запись',
        'text': 'Второй просто большой текст',
        'date': '10.01.2019',
    },
]


def home(request):
    data = {
        'news': news,
        'title': 'Main page of block'
    }
    return render(request, 'blog/home.html', data)


def block(request):
    return render(request, 'blog/block.html', {'title': 'Page about us'})
