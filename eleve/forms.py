from django import forms
from models import *

#formulaire permettant de récupérer les informations notées dans fields appartenant au modèle Enfant
class EnfantForm(forms.ModelForm):

	class Meta:
		model = Enfant
		fields = ('nom','prenom','classe','date','E1','E2','S1','S2','Nindiv','age')

#formulaire permettant de récupérer les informations notées dans fields appartenant au modèle EnfantComplete
class EnfantCompleteForm(forms.ModelForm):

	class Meta:
		model = EnfantComplete
		fields = ('nom','prenom','classe','date','E1','E2','S1','S2','Nindiv','age')
