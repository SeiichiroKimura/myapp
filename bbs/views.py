from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'welcome to bbs app',
        'players': ['勇者', '魔法使い', '剣士', 'サル'],
        'enemy': 'スライム'
        }
    return render(request, 'bbs/index.html', context)
