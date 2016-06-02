from django.contrib import admin
from eleve.models import *

class Enfantadmin(admin.ModelAdmin):
	list_display = ('date','lastname', 'firstname', 'classe')
	search_fields = ('lastname', 'firstname',)

admin.site.register(Enfant, Enfantadmin)
