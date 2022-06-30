from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Client
from django.contrib import messages


def home(request):
    clients = Client.objects.all()
    data = {'clients': clients}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_url')

        else:
            messages.add_message(request, messages.ERROR, 'Erro no login.')

    return render(request, 'Client_Registration/home.html', data)
