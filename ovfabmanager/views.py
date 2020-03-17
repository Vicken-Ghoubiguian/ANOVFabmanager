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

def common_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'common_tarifs_et_abonnements'})

def gestion_des_paniers(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gestion_des_paniers'})

def gestion_des_stocks(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gestion_des_stocks'})

def gerer_le_calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gerer_le_calendrier'})

def gerer_les_utilisateurs(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gerer_les_utilisateurs'})

def gerer_les_machines(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gerer_les_machines'})

def gerer_les_factures(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gerer_les_factures'})

def admin_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'admin_tarifs_et_abonnements'})

def gerer_les_espaces(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gerer_les_espaces'})

def suivi_des_formations(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'suivi_des_formations'})

def gerer_les_evenements(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'gerer_les_evenements'})

def statistiques(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'statistiques'})

def personnalisation(request):
    return render(request, 'ovfabmanager/index.html', {'template_demandee': 'personnalisation'})
