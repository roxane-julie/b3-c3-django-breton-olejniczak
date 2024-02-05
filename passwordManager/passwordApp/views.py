from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm, CreateNewSafeBox
from django.contrib.auth.hashers import make_password
from .models import SafeBox, PassWordManagerDataModel

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

def signIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Traitement des données du formulaire
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authentifier l'utilisateur
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Connecter l'utilisateur
                login(request, user)
                return redirect('myPasswordsManager')
            else:
                # Retourner une erreur si l'utilisateur n'est pas trouvé
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'signIn.html', {'form': form})

def signOut(request):
    logout(request)
    return redirect('index')

@login_required
def myPasswordsManager(request):
    if request.method == 'POST':
        form = CreateNewSafeBox(request.POST)
        if form.is_valid():
            new_safebox = SafeBox(name=form.cleaned_data['name'], user=request.user)
            new_safebox.save()
            return redirect('myPasswordsManager')
    else:
        form = CreateNewSafeBox()

    safeboxes = SafeBox.objects.filter(user=request.user)
    return render(request, 'myPasswordsManager.html', {'form': form, 'safeboxes': safeboxes})

# @login_required
# def addPasswordData(request, safebox_id):
#     safebox = SafeBox.objects.get(id=safebox_id, user=request.user)

#     if request.method == 'POST':
#         form = AddPasswordDataForm(request.POST)
#         if form.is_valid():
#             password_data = PassWordManagerDataModel(
#                 safebox=safebox
#                 website=form.cleaned_data['website'],
#                 password=form.cleaned_data['password'],
#             )
#             password_data.save()
#             return redirect('myPasswordsManager')
#     else:
#         form = AddPasswordDataForm()

#     return render(request, 'myPasswordManager.html', {'form': form})