from rest_framework import serializers
from .models import Enfant

class EnfantSerializer(serializers.ModelSerializer):
	#le serializer permet de convertir les donnée au format JSON

	class Meta:
		model = Enfant
		fields = ('Nindiv','lastname','firstname','date','classe','E1','E2','S1','S2')
