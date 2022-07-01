from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Client
from django.contrib import messages


def home(request):
    search = request.GET['search_input']

    if not bool(search):
        clients = Client.objects.all()
        data = {'clients': clients}
    else:
        first_name = list(Client.objects.filter(first_name__icontains=search))
        last_name = list(Client.objects.filter(last_name__icontains=search))
        age = list(Client.objects.filter(age__icontains=search))
        bio = list(Client.objects.filter(bio__icontains=search))

        clients = set(first_name + last_name + age + bio)
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

@login_required
def user_logout(request):
    logout(request)
    return redirect('home_url')