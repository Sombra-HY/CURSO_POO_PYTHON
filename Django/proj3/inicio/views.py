from django.shortcuts import render

# Create your views here.

def index( req):
    print(req)
    return render(req,'inicio/index.html')