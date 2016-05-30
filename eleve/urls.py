from django.conf.urls import url
from eleve import views




urlpatterns = [
    url(r'^enfants/$',views.liste),
    url(r'^enfants/(?P<Nindiv>[a-zA-Z0-9_;-]+)$',views.details)
]

