from django.contrib import admin
from eleve.models import *

class Enfantadmin(admin.ModelAdmin):
    list_display = ('date','lastname', 'firstname', 'classe')

admin.site.register(Enfant, Enfantadmin)
