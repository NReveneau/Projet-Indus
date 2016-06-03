from django.conf.urls import url
from eleve import views




urlpatterns = [
	url(r'^enfant/$', views.enfant_list, name = 'afficher_enfant'),
	url(r'^ajouterenfant/$', views.ajouterEnfant, name = 'ajouter_enfant'),
	url(r'^enfantcomplete/$', views.enfantcomplete_list, name = 'afficher_enfantcomplete'),
	url(r'^ajouterenfantcomplete/$', views.ajouterEnfantComplete, name = 'ajouter_enfantcomplete'),
    url(r'^json/$',views.liste),
    url(r'^json/(?P<Nindiv>[a-zA-Z0-9_;-]+)$',views.details),
    url(r'^jsoncomplete/$',views.listeComplete),
    url(r'^jsoncomplete/(?P<Nindiv>[a-zA-Z0-9_;-]+)$',views.detailsComplete)
]

