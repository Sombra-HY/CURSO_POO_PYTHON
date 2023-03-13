from django.shortcuts import render

def index_inicial(request):
    return render(request, 'home/index.html')