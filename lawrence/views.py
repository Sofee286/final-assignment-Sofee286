from django.shortcuts import render


def home(request):
    return render(request,'lawrence/home.html')

def contact(request):
    return render(request,'lawrence/contract.html')

def aboutmontessori(request):
    return render(request,'lawrence/aboutmontessori.html')

