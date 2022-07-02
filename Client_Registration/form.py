from django.forms import ModelForm
from .models import Client


class Client_Form(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'age', 'bio', 'image']
