from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'index'})

def calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'calendrier'})
