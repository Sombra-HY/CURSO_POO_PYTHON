from . import views
from django.urls import path
# blog/ caminho 
urlpatterns = [
    path('',views.index) # referencia do renderizador
]
