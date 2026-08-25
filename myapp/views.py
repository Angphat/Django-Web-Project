from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home.html")

def unicafe(request):
    return render(request, "unicafe/index.html")
