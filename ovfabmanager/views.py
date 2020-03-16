from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'accueil'})

def calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'calendrier'})
