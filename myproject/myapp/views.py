"""
Este módulo contiene las vistas (views) para tu aplicación.
"""

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
