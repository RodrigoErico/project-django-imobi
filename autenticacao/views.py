from django.shortcuts import render, redirect
from django.http import HttpResponse


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('/auth/cadastro')

        return HttpResponse(f'{username} {email} {password}')


def login(request):
    return HttpResponse('Login')
