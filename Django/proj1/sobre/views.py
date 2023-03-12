from django.shortcuts import render

# Create your views here.

def incial (req):
    return render(req , 'sobre/index.html')