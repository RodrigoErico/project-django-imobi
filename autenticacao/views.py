from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return HttpResponse(f'{username} {email} {password}')


def login(request):
    return HttpResponse('Login')
