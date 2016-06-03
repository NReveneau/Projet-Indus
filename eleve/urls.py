from django.conf.urls import url
from eleve import views




urlpatterns = [
	#création d'une adresse pour l'affichage de la liste des enfants avant pointage
	url(r'^enfant/$', views.enfant_list, name = 'afficher_enfant'),
	#création d'une adresse pour l'affichage du formulaire de création des enfants avant pointage
	url(r'^ajouterenfant/$', views.ajouterEnfant, name = 'ajouter_enfant'),
	#création d'une adresse pour l'affichage de la liste des enfants après pointage
	url(r'^enfantcomplete/$', views.enfantcomplete_list, name = 'afficher_enfantcomplete'),
	#création d'une adresse pour l'affichage ddu formulaire de création des enfants après pointage
	url(r'^ajouterenfantcomplete/$', views.ajouterEnfantComplete, name = 'ajouter_enfantcomplete'),
	#création d'une adresse pour l'affichage de la page des méthodes GET et POST pour le modèle Enfant
 	url(r'^json/$',views.liste),
 	#création d'une adresse pour l'affichage de la page des méthodes GET, PUT et DELETE pour le modèle Enfant
    	url(r'^json/(?P<Nindiv>[a-zA-Z0-9_;-]+)$',views.details),
    	#création d'une adresse pour l'affichage de la page des méthodes GET et POST pour le modèle EnfantComplete
    	url(r'^jsoncomplete/$',views.listeComplete),
    	#création d'une adresse pour l'affichage de la page des méthodes GET, PUT et DELETE pour le modèle EnfantComplete
    	url(r'^jsoncomplete/(?P<Nindiv>[a-zA-Z0-9_;-]+)$',views.detailsComplete)
]

