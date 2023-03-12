from django.shortcuts import render

# Create your views here.

def index(resq):
    return render(resq,'index.html') 