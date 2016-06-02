from django import forms
from models import Enfant

class EnfantForm(forms.ModelForm):

	class Meta:
		model = Enfant
		fields = ('lastname','firstname','classe','date','E1','E2','S1','S2','Nindiv')