from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Client
from django.contrib import messages
from django.db.models import Q

def home(request):
    search = request.GET['search_input']

    if not bool(search):
        clients = Client.objects.all()
        data = {'clients': clients}
    else:
        clients = Client.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search) |
                                        Q(age__icontains=search) | Q(bio__icontains=search))
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