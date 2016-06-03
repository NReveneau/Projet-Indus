from rest_framework import serializers
from .models import *

class EnfantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Enfant
		fields = ('Nindiv','nom','prenom','date','classe','E1','E2','S1','S2','age')


class EnfantCompleteSerializer(serializers.ModelSerializer):

	class Meta:
		model = EnfantComplete
		fields = ('Nindiv','nom','prenom','date','classe','E1','E2','S1','S2','age')
