from django import forms
from models import *

class EnfantForm(forms.ModelForm):

	class Meta:
		model = Enfant
		fields = ('nom','prenom','classe','date','E1','E2','S1','S2','Nindiv','age')


class EnfantCompleteForm(forms.ModelForm):

	class Meta:
		model = EnfantComplete
		fields = ('nom','prenom','classe','date','E1','E2','S1','S2','Nindiv','age')