from django.shortcuts import render
from django.shortcuts import redirect

from .models import Abonnement
from .models import Article
from .models import Panier
from .models import Client
from .models import Carte
from .models import Type_de_client
from .models import Prestation

import html, hashlib

allClients = Client.objects.all()
allAbonnements = Abonnement.objects.all()
allPaniers = Panier.objects.all()
allArticles = Article.objects.all()

# For forms treatments...
def form_treatments(request):

    if request.method == "GET":

      print("GET method....\n")

    elif request.method == "POST":

      print("POST method....\n")

      redirection_response = render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': 'formulaire non trouvé', 'template_demandee': None})

      data = request.POST.copy()

      # Traitements pour le formulaire de connexion...
      if data.get("form_type") == "connexion":

          print("\n ----------Formulaire: " + data.get("form_type") + "----------\n")
          print("\n Nom d'utilisateur = " + data.get("nom_d_utilisateur")  + "\n")
          print("\n Mot de passe = " + data.get("mot_de_passe")  + "\n")

          #
          redirection_response = redirect("/")

      # Traitements pour le formulaire d'inscription...
      elif data.get("form_type") == "inscription":

          #
          motDePasse = hashlib.md5(str.encode(data.get("mot_de_passe")))

          #
          nouveauClient = Client(nom_de_famille = data.get("nom").upper(), prenom = data.get("prenom"), telephone = data.get("telephone"), adresse_email = data.get("adresse_email"), identifiant = data.get("nom_d_utilisateur"), mot_de_passe = motDePasse.hexdigest(), credit_client_en_temps = 0)

          #
          nouveauClient.save()

          #
          redirection_response = redirect("/")

      # Traitements pour le formulaire des enregistrements de paniers...
      elif data.get("form_type") == "enregistrement_panier":

          #
          print("\n ----------Formulaire: " + data.get("form_type") + "----------\n")
          print("\n Client (numéro) = " + data.get("client_pret") + "\n")
          print("\n Date de retour = " + data.get("date_de_retour_du_pret") + "\n")
          print("\n Liste des articles = " + data.get("liste_des_articles_a_preter") + "\n")

          #
          redirection_response = redirect("/gestion_des_paniers#enregistrement_d_un_pret")

      # Traitements pour le formulaire des retours de paniers...
      elif data.get("form_type") == "retour_panier":

          #
          print("\n ----------Formulaire: " + data.get("form_type") + "----------\n")
          print("\n Client (numéro) = " + data.get("client_retour") + "\n")
          print("\n Liste des articles = " + data.get("liste_des_articles_a_retourner") + "\n")

          #
          redirection_response = redirect("/gestion_des_paniers#enregistrement_d_un_retour")

      # Traitements pour le formulaire d'enregistrement de produits...
      elif data.get("form_type") == "enregistrement_produit":

          #
          print("\n ----------Formulaire: " + data.get("form_type") + "----------\n")
          print("\n Code barre = " + data.get("codebarre") + "\n")
          print("\n Date d'achat = " + data.get("date_d_achat") + "\n")
          print("\n Date de livraison = " + data.get("date_de_livraison") + "\n")
          print("\n Type d'objet (numéro) = " + data.get("type_d_objet") + "\n")

          if data.get("nouveau_produit") == 'on':

            #
            print("\n Nouveau produit ? = " + data.get("nouveau_produit") + "\n")

            #
            print("\n Fabricant = " + data.get("fabricant") + "\n")
            print("\n Adresse email du fabricant = " + data.get("adresse_email_fabricant") + "\n")
            print("\n Adresse postale du fabricant = " + data.get("adresse_postale_fabricant") + "\n")
            print("\n Numéro de téléphone du fabricant = " + data.get("numero_telephone_fabricant") + "\n")
            print("\n Site web du fabricant = " + data.get("site_web_fabricant") + "\n")

            #
            print("\n Fournisseur = " + data.get("fournisseur") + "\n")
            print("\n Adresse email du fournisseur = " + data.get("adresse_email_fournisseur") + "\n")
            print("\n Adresse postale du fournisseur = " + data.get("adresse_postale_fournisseur") + "\n")
            print("\n Numéro de téléphone du fournisseur = " + data.get("numero_telephone_fournisseur") + "\n")
            print("\n Site web du fournisseur = " + data.get("site_web_fournisseur") + "\n")

          #
          redirection_response = redirect("/gestion_des_stocks#enregistrer_un_article_dans_les_stocks")

      else:

          print("\n Formulaire non trouvé : désolé... \n")

          redirection_response = render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': 'formulaire non trouvé', 'template_demandee': None, 'allAbonnements': allAbonnements})

    else:

      print("Other method....\n")

    return redirection_response

# For common
def accueil(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'accueil', 'allAbonnements': allAbonnements})

def calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'calendrier', 'allAbonnements': allAbonnements})

def reserver_une_machine(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'reserver_une_machine', 'allAbonnements': allAbonnements})

def reserver_un_espace(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'reserver_un_espace', 'allAbonnements': allAbonnements})

def inscriptions_aux_formations(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'inscriptions_aux_formations', 'allAbonnements': allAbonnements})

def inscriptions_aux_evenements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'inscriptions_aux_evenements', 'allAbonnements': allAbonnements})

def galerie_de_projets(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'galerie_de_projets', 'allAbonnements': allAbonnements})

def common_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'common_tarifs_et_abonnements', 'allAbonnements': allAbonnements})

# For admin
def gestion_des_paniers(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gestion_des_paniers', 'allAbonnements': allAbonnements, 'allClients': allClients, 'allPaniers': allPaniers, 'allArticles': allArticles})

def gestion_des_stocks(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gestion_des_stocks', 'allAbonnements': allAbonnements, 'allArticles': allArticles})

def gerer_le_calendrier(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_le_calendrier', 'allAbonnements': allAbonnements})

def gerer_les_utilisateurs(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_utilisateurs', 'allAbonnements': allAbonnements})

def gerer_les_machines(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_machines', 'allAbonnements': allAbonnements})

def gerer_les_factures(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_factures', 'allAbonnements': allAbonnements})

def admin_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'admin_tarifs_et_abonnements', 'allAbonnements': allAbonnements})

def gerer_les_espaces(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_espaces', 'allAbonnements': allAbonnements})

def suivi_des_formations(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'suivi_des_formations', 'allAbonnements': allAbonnements})

def gerer_les_evenements(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'gerer_les_evenements', 'allAbonnements': allAbonnements})

def statistiques(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'statistiques', 'allAbonnements': allAbonnements})

def personnalisation(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': False, 'type_erreur': None, 'template_demandee': 'personnalisation', 'allAbonnements': allAbonnements})

#For errors
def error_500(request):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '404', 'template_demandee': None, 'allAbonnements': allAbonnements})

def error_410(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '410', 'template_demandee': None, 'allAbonnements': allAbonnements})

def error_408(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '408', 'template_demandee': None, 'allAbonnements': allAbonnements})

def error_404(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '404', 'template_demandee': None, 'allAbonnements': allAbonnements})

def error_403(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '403', 'template_demandee': None, 'allAbonnements': allAbonnements})

def error_401(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '401', 'template_demandee': None, 'allAbonnements': allAbonnements})

def error_400(request, exception):
    return render(request, 'ovfabmanager/index.html', {'afficher_erreur': True, 'type_erreur': '400', 'template_demandee': None, 'allAbonnements': allAbonnements})
