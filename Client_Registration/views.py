from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Client
from .form import Client_Form
from django.contrib import messages
from django.db.models import Q

def home(request):
    search = request.GET.get('search_input')

    if not search:
        clients = Client.objects.all()
        data = {'clients': clients}
    else:
        search = search.strip()
        clients = Client.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search) |
                                        Q(age__icontains=search) | Q(bio__icontains=search))
        data = {'clients': clients}

    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
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

@login_required
def add_product(request):
    form = Client_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home_url')

    data = {'form': form}
    return render(request, 'Client_Registration/add_product.html', data)

@login_required
def update(request, id):
    client = Client.objects.get(pk=id)
    form = Client_Form(request.POST or None, request.FILES or None, instance=client)
    print(f'imagem: {client.image}')
    if form.is_valid():
        form.save()
        return redirect('home_url')

    data = {'form': form, 'client_id': id, 'client_image': client.image}
    return render(request, 'Client_Registration/edit_product.html', data)

@login_required
def delete(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('home_url')
