from django.shortcuts import render

# Create your views here.
def clients_list(request):
    return render(request, "client/clients_list.html")