from django.shortcuts import render
from django.shortcuts import render, redirect

from .forms import AddClientForm
from .models import Client

# Create your views here.
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)

    return render (request, 'client/clients_list.html', { 
        'clients' : clients
    })

def add_clients(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')

        Client.objects.create(
            name=name,
            email=email,
            description=description,

            created_by=request.user
        )
        return redirect('clients_list')

    return render(request, 'client/add_client.html')