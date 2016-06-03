from django.contrib import admin
from eleve.models import *

class Enfantadmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'classe')

admin.site.register(Enfant, Enfantadmin)

class EnfantCompleteadmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'classe')

admin.site.register(EnfantComplete, EnfantCompleteadmin)
