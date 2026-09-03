from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def unicafe(request):
    return render(request, "unicafe/index.html")

@login_required
def account(request):
    return render(request, 'myapp/account.html')
