from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Esto guardará los datos en la base de datos
            return redirect('home')  # Redirige a la página de inicio después del registro exitoso
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
