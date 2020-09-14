from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers

from .models import Abonnement
from .models import Article
from .models import Panier
from .models import Client
from .models import Carte
from .models import Type_de_client
from .models import Prestation
from .models import Outil
from .models import Etat

import hashlib, datetime

allClients = Client.objects.all()
allCartes = Carte.objects.all()
allAbonnements = Abonnement.objects.all()
allPaniers = Panier.objects.all()
allArticles = Article.objects.all()
allOutils = Outil.objects.all()

allSerializedArticles = serializers.serialize('json', allArticles)
allSerializedClients = serializers.serialize('json', allClients)
allSerializedCartes = serializers.serialize('json', allCartes)
allSerializedPaniers = serializers.serialize('json', allPaniers)

#
def contextFunction(afficher_erreur, type_erreur, template_demandee):
    return {'afficher_erreur': afficher_erreur, 'type_erreur': type_erreur, 'template_demandee': template_demandee, 'allAbonnements': allAbonnements, 'allSerializedArticles': allSerializedArticles, 'allSerializedClients': allSerializedClients, 'allSerializedCartes': allSerializedCartes, 'allSerializedPaniers': allSerializedPaniers, 'allClients': allClients, 'allCartes': allCartes, 'allPaniers': allPaniers, 'allArticles': allArticles, 'allOutils': allOutils}

# For forms treatments...
def form_treatments(request):

    if request.method == "GET":

      print("GET method....\n")

    elif request.method == "POST":

      print("POST method....\n")

      redirection_response = render(request, 'ovfabmanager/index.html', contextFunction(True, 'formulaire non trouvé', None))

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
          numeroCarteClient = data.get("client_retour")

          #
          listeDesArticlesARetourner = data.get("liste_des_articles_a_retourner")

          #
          listeDesArticlesARetourner = listeDesArticlesARetourner.split(",\r\n")

          #
          listeDesArticlesARetourner.pop()

          #
          listeDesArticlesARetournerParCodeBarre = []

          #
          for article in listeDesArticlesARetourner:

                #
                articleCommeListe = article.split(" ")

                codeBarreBrut = articleCommeListe[len(articleCommeListe) - 1]

                #
                nombreFinal = len(codeBarreBrut) - 1

                #
                listeDesArticlesARetournerParCodeBarre.append(codeBarreBrut[1:nombreFinal])

          #
          carteDuClientConcerne = Carte.objects.get(numero_de_carte = numeroCarteClient)

          #
          clientConcerne = Client.objects.get(carte = carteDuClientConcerne)

          #
          panierConcerne = Panier.objects.get(client = clientConcerne)

          #
          for article in Article.objects.filter(panier = panierConcerne):

                #
                if article.code_barre in listeDesArticlesARetournerParCodeBarre:

                      #
                      article.panier = None

                      #
                      article.save()

          #
          redirection_response = redirect("/gestion_des_paniers#enregistrement_d_un_retour")

      # Traitements pour le formulaire d'enregistrement de produits...
      elif data.get("form_type") == "enregistrement_produit":

          #
          if data.get("nouveau_produit") == 'on':

              #
              nouvelOutil = Outil(libelle = data.get("outil"), description = data.get("description_outil"), fabricant = data.get("fabricant"), fournisseur = data.get("fournisseur"))

              #
              nouvelOutil.save()
              
              #
              date_d_achat = datetime.datetime.strptime(data.get("date_d_achat"), '%d/%m/%Y').strftime("%Y-%m-%d")
              date_de_livraison = datetime.datetime.strptime(data.get("date_de_livraison"), '%d/%m/%Y').strftime("%Y-%m-%d")

              #
              nouvelArticle = Article(code_barre = data.get("codebarre"), libelle = data.get("libelle"), date_d_achat = date_d_achat, date_de_livraison = date_de_livraison, outil = nouvelOutil)

              #
              nouvelArticle.save()

          #
          else:
          
              #
              outilCorrespondant = Outil.objects.get(pk = data.get("type_d_objet"))
              
              #
              date_d_achat = datetime.datetime.strptime(data.get("date_d_achat"), '%d/%m/%Y').strftime("%Y-%m-%d")
              date_de_livraison = datetime.datetime.strptime(data.get("date_de_livraison"), '%d/%m/%Y').strftime("%Y-%m-%d")

              #
              nouvelArticle = Article(code_barre = data.get("codebarre"), libelle = data.get("libelle"), date_d_achat = date_d_achat, date_de_livraison = date_de_livraison, outil = outilCorrespondant)

              #
              nouvelArticle.save()

          #
          redirection_response = redirect("/gestion_des_stocks#enregistrer_un_article_dans_les_stocks")

      else:

          print("\n Formulaire non trouvé : désolé... \n")

          redirection_response = render(request, 'ovfabmanager/index.html', contextFunction(True, 'formulaire non trouvé', None))

    else:

      print("Other method....\n")

    return redirection_response

# For common
def accueil(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'accueil'))

def calendrier(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'calendrier'))

def reserver_une_machine(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'reserver_une_machine'))

def reserver_un_espace(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'reserver_un_espace'))

def inscriptions_aux_formations(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'inscriptions_aux_formations'))

def inscriptions_aux_evenements(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'inscriptions_aux_evenements'))

def galerie_de_projets(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'galerie_de_projets'))

def common_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'common_tarifs_et_abonnements'))

# For admin
def gestion_des_paniers(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gestion_des_paniers'))

def gestion_des_stocks(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gestion_des_stocks'))

def gerer_le_calendrier(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gerer_le_calendrier'))

def gerer_les_utilisateurs(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gerer_les_utilisateurs'))

def gerer_les_machines(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gerer_les_machines'))

def gerer_les_factures(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gerer_les_factures'))

def admin_tarifs_et_abonnements(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'admin_tarifs_et_abonnements'))

def gerer_les_espaces(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gerer_les_espaces'))

def suivi_des_formations(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'suivi_des_formations'))

def gerer_les_evenements(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'gerer_les_evenements'))

def statistiques(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'statistiques'))

def personnalisation(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(False, None, 'personnalisation'))

#For errors
def error_500(request):
    return render(request, 'ovfabmanager/index.html', contextFunction(True, '500', None))

def error_410(request, exception):
    return render(request, 'ovfabmanager/index.html', contextFunction(True, '410', None))

def error_408(request, exception):
    return render(request, 'ovfabmanager/index.html', contextFunction(True, '408', None))

def error_404(request, exception):
    return render(request, 'ovfabmanager/index.html', contextFunction(True, '404', None))

def error_403(request, exception):
    return render(request, 'ovfabmanager/index.html', contextFunction(True, '403', None))

def error_401(request, exception):
    return render(request, 'ovfabmanager/index.html', contextFunction(True, '401', None))

def error_400(request, exception):
    return render(request, 'ovfabmanager/index.html', contextFunction(True, '400', None))
