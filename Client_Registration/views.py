from django.shortcuts import render
from .models import Client

# Create your views here.
def home(request):
    clients = Client.objects.all()
    data = {'clients': clients}
    return render(request, 'Client_Registration/home.html', data)