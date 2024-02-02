from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def signIn(request):
    return render(request, 'signIn.html')

def myPasswordsManager(request):
    return render(request, 'myPasswordsManager.html')

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Traitement des données du formulaire
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Hacher le mot de passe avant de le stocker
            hashed_password = make_password(password)

            # Créer un nouvel utilisateur
            new_user = User.objects.create(username=username, email=email, password=hashed_password)

            return redirect('success')
    else:
        form = SignUpForm()

    return render(request, 'signUp.html', {'form': form})