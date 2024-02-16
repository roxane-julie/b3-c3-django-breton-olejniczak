from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm, CreateNewSafeBox, CreateNewCard
from django.contrib.auth.hashers import make_password
from .models import SafeBox, PassWordManagerDataModel
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def signIn(request):
    return render(request, 'signIn.html')

def myPasswordsManager(request):
    return render(request, 'myPasswordsManager.html')

def safeBoxContainer(request):
    return render(request, 'safeBoxContainer.html', {'active_tab': 'manager'})

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

    return render(request, 'signUp.html', {'form': form, 'active_tab': 'signUp'})

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

    return render(request, 'signIn.html', {'form': form, 'active_tab': 'signIn'})

def signOut(request):
    logout(request)
    return redirect('index')

@login_required
def myPasswordsManager(request):
    print(request)
    name = request.GET.get('name', None)
    safebox_id = request.GET.get('id', None)
    print(name)

    if request.method == 'POST':
        form = CreateNewSafeBox(request.POST)
        if form.is_valid():
            new_safebox = SafeBox(name=form.cleaned_data['name'], user=request.user)
            new_safebox.save()
            data = {
                'success': True,
                'message': 'Le coffre-fort a été créé avec succès.',
                'safebox': {
                'id': new_safebox.id,
                'name': new_safebox.name,
            }
         }
            return JsonResponse(data)
        else:
            data = {'success': False, 'errors': form.errors}
        return JsonResponse(data)
    else:
        form = CreateNewSafeBox()

    safeboxes = SafeBox.objects.filter(user=request.user)
    safebox_count = SafeBox.objects.count()

    return render(request, 'myPasswordsManager.html', {'form': form, 'safeboxes': safeboxes, 'name': name, 'id': safebox_id, 'active_tab': 'manager', 'safebox_count': safebox_count})

@login_required
def deleteSafebox(request, safebox_id):
    print('Cest la fonction delete')
    print(f"deleteSafebox called with method {request.method} and safebox_id {safebox_id}")
    if request.method == 'DELETE':
        try:
            safebox = SafeBox.objects.get(id=safebox_id, user=request.user)
        except SafeBox.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Coffre-fort non trouvé.'})

        safebox.delete()
        return JsonResponse({'success': True, 'message': 'Coffre-fort supprimé avec succès.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def safeBoxContainer(request):
    passwordDatas = PassWordManagerDataModel.objects.all()
    return render(request, 'safeBoxContainer.html', {'passwordDatas': passwordDatas})

def get_password_data(request):
    safebox_id = request.GET.get('id')
    safebox = get_object_or_404(SafeBox, id=safebox_id)
    password_data = safebox.passwords.all().values('websiteName', 'websiteUrl', 'password')
    return JsonResponse(list(password_data), safe=False)

@login_required    
def createNewCard(request):
    if request.method == 'POST':
        form = CreateNewCard(request.POST)
        if form.is_valid():
            websiteName = form.cleaned_data['websiteName']
            websiteUrl = form.cleaned_data['websiteUrl']
            password = form.cleaned_data['password']
            user = request.user

            hashed_password = make_password(password)

            try:
                new_passwordData = PassWordManagerDataModel.objects.create(
                    websiteName=websiteName, websiteUrl=websiteUrl, password=hashed_password,
                    user=user)
                data = {
                    'success': True,
                    'message': "La carte d'informations de votre mot de passe a été créée avec succès",
                    'passwordData': {
                        'id': new_passwordData.id,
                        'websiteName': new_passwordData.websiteName,
                        'websiteUrl': new_passwordData.websiteUrl,
                        'password': new_passwordData.password
                    }
                }
                return JsonResponse(data)
            except Exception as e:
                # Gérer l'erreur ici
                print(f"Erreur lors de la création de la nouvelle carte : {e}")
                data = {
                    'success': False,
                    'message': f"Erreur lors de la création de la nouvelle carte : {e}",
                }
                return JsonResponse(data, status=500)
        else:
            # Le formulaire n'est pas valide
            data = {
                'success': False,
                'message': "Le formulaire n'est pas valide",
            }
            return JsonResponse(data, status=400)
    else:
        # La requête n'est pas une requête POST
        data = {
            'success': False,
            'message': "La requête n'est pas une requête POST",
        }
        return JsonResponse(data)