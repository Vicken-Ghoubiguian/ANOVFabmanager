from django.urls import path
from . import views

urlpatterns = [

    # For treatments
    path('form_treatments', views.form_treatments, name='form_treatments'),

    # For common
    path('', views.accueil, name='accueil'),
    path('calendrier', views.calendrier, name='calendrier'),
    path('reserver_une_machine', views.reserver_une_machine, name='reserver_une_machine'),
    path('reserver_un_espace', views.reserver_un_espace, name='reserver_un_espace'),
    path('inscriptions_aux_formations', views.inscriptions_aux_formations, name='inscriptions_aux_formations'),
    path('inscriptions_aux_evenements', views.inscriptions_aux_evenements, name='inscriptions_aux_evenements'),
    path('galerie_de_projets', views.galerie_de_projets, name='galerie_de_projets'),
    path('common_tarifs_et_abonnements', views.common_tarifs_et_abonnements, name='common_tarifs_et_abonnements'),

    # For admin
    path('gestion_des_paniers', views.gestion_des_paniers, name='gestion_des_paniers'),
    path('gestion_des_stocks', views.gestion_des_stocks, name='gestion_des_stocks'),
    path('gerer_le_calendrier', views.gerer_le_calendrier, name='gerer_le_calendrier'),
    path('gerer_les_utilisateurs', views.gerer_les_utilisateurs, name='gerer_les_utilisateurs'),
    path('gerer_les_machines', views.gerer_les_machines, name='gerer_les_machines'),
    path('gerer_les_factures', views.gerer_les_factures, name='gerer_les_factures'),
    path('admin_tarifs_et_abonnements', views.admin_tarifs_et_abonnements, name='admin_tarifs_et_abonnements'),
    path('gerer_les_espaces', views.gerer_les_espaces, name='gerer_les_espaces'),
    path('suivi_des_formations', views.suivi_des_formations, name='suivi_des_formations'),
    path('gerer_les_evenements', views.gerer_les_evenements, name='gerer_les_evenements'),
    path('statistiques', views.statistiques, name='statistiques'),
    path('personnalisation', views.personnalisation, name='personnalisation'),
]

#######################################################################################################################
# Définitions des handlers pour un traitement customisé des différents types d'erreurs (HTTP ou non) rencontrées...
#
# PS: pour activer ce dispositif en mode dév (développement de l'application), allez dans le fichier 'settings.py'
# situé dans le répertoire ../ANOVFabmanager puis modifiez la valeur spécifiée pour 'DEBUG' de 'True' à 'False'.
#######################################################################################################################

handler404 = "ovfabmanager.views.error_404"
handler500 = "ovfabmanager.views.error_500"
handler408 = "ovfabmanager.views.error_408"
handler403 = "ovfabmanager.views.error_403"
handler410 = "ovfabmanager.views.error_410"
handler401 = "ovfabmanager.views.error_401"
handler400 = "ovfabmanager.views.error_400"
