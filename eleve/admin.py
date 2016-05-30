from django.contrib import admin
from eleve.models import *

class Enfantadmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'classe')

admin.site.register(Enfant, Enfantadmin)
