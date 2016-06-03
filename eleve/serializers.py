from rest_framework import serializers
from .models import *

#serializer permettant la traduction des fields depuis le modèle Enfant en Json et inversement
class EnfantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Enfant
		fields = ('Nindiv','nom','prenom','date','classe','E1','E2','S1','S2','age')

#serializer permettant la traduction des fields depuis le modèle EnfantComplete en Json et inversement
class EnfantCompleteSerializer(serializers.ModelSerializer):

	class Meta:
		model = EnfantComplete
		fields = ('Nindiv','nom','prenom','date','classe','E1','E2','S1','S2','age')
