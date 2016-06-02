from django.conf.urls import url
from eleve import views




urlpatterns = [
	url(r'^enfants/$', views.enfant_list, name = 'ajouter_enfant'),
    url(r'^json/$',views.liste),
    url(r'^json/(?P<Nindiv>[a-zA-Z0-9_;-]+)$',views.details)
]

