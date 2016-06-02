from django.shortcuts import render
from forms import EnfantForm
from .serializers import EnfantSerializer
from .models import Enfant
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def enfant_list(request):
	enfants=Enfant.objects.all()
	return render(request,'appli/enfant_liste.html',{'enfants': enfants})

def AjouterEnfant(request):
	form =  EnfantForm()
	return render(request,'appli/ajouter_enfant.html',{'form': form})




























@api_view(['GET','POST'])
def liste(request):

	if request.method == 'GET':
		enfants = Enfant.objects.all()
		serializer = EnfantSerializer(enfants, many = True)
		return Response(serializer.data)

	elif request.method == 'POST' :
		serializer = EnfantSerializer(data = request.data, many = True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def details(request, Nindiv):

	try :
		enfant = Enfant.objects.get(Nindiv = Nindiv)
	except Enfant.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = EnfantSerializer(enfant)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = EnfantSerializer(enfant, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		enfant.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
