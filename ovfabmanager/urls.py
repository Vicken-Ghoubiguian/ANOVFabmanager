from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('calendrier', views.calendrier, name='calendrier'),
    path('reserver_une_machine', views.reserver_une_machine, name='reserver_une_machine'),
    path('reserver_un_espace', views.reserver_un_espace, name='reserver_un_espace'),
    path('inscriptions_aux_formations', views.inscriptions_aux_formations, name='inscriptions_aux_formations'),
    path('inscriptions_aux_evenements', views.inscriptions_aux_evenements, name='inscriptions_aux_evenements'),
    path('galerie_de_projets', views.galerie_de_projets, name='galerie_de_projets'),
    path('common_tarifs_et_abonnements', views.common_tarifs_et_abonnements, name='common_tarifs_et_abonnements'),
]
