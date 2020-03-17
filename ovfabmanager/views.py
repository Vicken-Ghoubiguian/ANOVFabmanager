from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'accueil'})

def calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'calendrier'})

def reserver_une_machine(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'reserver_une_machine'})

def reserver_un_espace(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'reserver_un_espace'})

def inscriptions_aux_formations(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'inscriptions_aux_formations'})

def inscriptions_aux_evenements(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'inscriptions_aux_evenements'})

def galerie_de_projets(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'galerie_de_projets'})

def tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'tarifs_et_abonnements'})
