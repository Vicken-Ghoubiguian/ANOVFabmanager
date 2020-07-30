from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def connexion(request):
    if request.method == "GET":
      print("GET method....\n")

    elif request.method == "POST":
      print("POST method....\n")

      data = request.POST.copy()

      if data.get("form_type") == "connexion":

          print("\n ----------Formulaire: " + data.get("form_type") + "----------\n")
          print("\n Nom d'utilisateur = " + data.get("nom_d_utilisateur")  + "\n")
          print("\n Mot de passe = " + data.get("mot_de_passe")  + "\n")

      elif data.get("form_type") == "inscription":

          print("\n ----------Formulaire: " + data.get("form_type") + "----------\n")
          print("\n Nom d'utilisateur = " + data.get("nom")  + "\n")
          print("\n Mot de passe = " + data.get("prenom")  + "\n")
          print("\n Et les autres champs ? À venir bientôt... \n")

    else:
      print("Other method....\n")

    redirection_response = redirect("/")

    return redirection_response

def enregistrer_produit(request):

    print("This is the end of my only friend....")

    redirection_response = redirect("/gestion_des_stocks")

    return redirection_response

# For common
def accueil(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'accueil'})

def calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'calendrier'})

def reserver_une_machine(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'reserver_une_machine'})

def reserver_un_espace(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'reserver_un_espace'})

def inscriptions_aux_formations(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'inscriptions_aux_formations'})

def inscriptions_aux_evenements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'inscriptions_aux_evenements'})

def galerie_de_projets(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'galerie_de_projets'})

def common_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'common_tarifs_et_abonnements'})

# For admin
def gestion_des_paniers(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gestion_des_paniers'})

def gestion_des_stocks(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gestion_des_stocks'})

def gerer_le_calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_le_calendrier'})

def gerer_les_utilisateurs(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_utilisateurs'})

def gerer_les_machines(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_machines'})

def gerer_les_factures(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_factures'})

def admin_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'admin_tarifs_et_abonnements'})

def gerer_les_espaces(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_espaces'})

def suivi_des_formations(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'suivi_des_formations'})

def gerer_les_evenements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_evenements'})

def statistiques(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'statistiques'})

def personnalisation(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'personnalisation'})

#For errors
def error_500(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '404', 'template_demandee': None})

def error_410(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '410', 'template_demandee': None})

def error_408(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '408', 'template_demandee': None})

def error_404(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '404', 'template_demandee': None})

def error_403(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '403', 'template_demandee': None})

def error_401(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '401', 'template_demandee': None})

def error_400(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '400', 'template_demandee': None})
