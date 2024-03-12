from django.shortcuts import render, redirect
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al usuario al inicio de sesión después del registro
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
