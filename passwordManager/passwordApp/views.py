from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'signUp.html')

def signIn(request):
    return render(request, 'signIn.html')