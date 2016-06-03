from django.shortcuts import render
from django.shortcuts import redirect
from forms import *
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, date


#permet l'affichage de la liste des entrées dans Enfant pour l'interface graphique
def enfant_list(request):
	enfants=Enfant.objects.all()
	return render(request,'appli/enfant_liste.html',{'enfants': enfants})
	
#permet l'affichage de la liste des entrées dans EnfantComplete pour l'interface graphique
def enfantcomplete_list(request):
	enfantscomplete=EnfantComplete.objects.all()
	return render(request,'appli/enfantcomplete_liste.html',{'enfantscomplete': enfantscomplete})

#permet l'affichage du formulaire d'ajout d'entrées dans Enfant depuis l'interface graphique et redirection après POST
def ajouterEnfant(request):
	if request.method == "POST":
		form=EnfantForm(request.POST)
		if form.is_valid():
			enfant = form.save(commit=False)
			enfant.save()
			return redirect('eleve.views.enfant_list')
	else:
		form=EnfantForm()
		return render(request, 'appli/ajouter_enfant.html', {'form':form})

#permet l'affichage du formulaire d'ajout d'entrées dans EnfantComplete depuis l'interface graphique et redirection après POST
def ajouterEnfantComplete(request):
	if request.method == "POST":
		form=EnfantCompleteForm(request.POST)
		if form.is_valid():
			enfant = form.save(commit=False)
			enfant.save()
			return redirect('eleve.views.enfantcomplete_list')
	else:
		form=EnfantCompleteForm()
		return render(request, 'appli/ajout_enfantcomplete.html', {'form':form})



#view permettant l'affichage de la page donnant et récupérant les Json pour le modèle Enfant
@api_view(['GET','POST'])
def liste(request):

	today=date.today()

	if request.method == 'GET':
		enfants = Enfant.objects.filter(date=today)
		serializer = EnfantSerializer(enfants, many = True)
		return Response(serializer.data)

	elif request.method == 'POST' :
		serializer = EnfantSerializer(data = request.data, many = True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#non utilisé pour l'instant mais peut être utile pour effectuer des opérations sur un seul enfant à partir d'un format json.(Enfant)
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


#view permettant l'affichage de la page donnant et récupérant les Json pour le modèle EnfantComplete
@api_view(['GET','POST'])
def listeComplete(request):

	if request.method == 'GET':
		enfantsComplete = EnfantComplete.objects.all()
		serializer = EnfantCompleteSerializer(enfantsComplete, many = True)
		return Response(serializer.data)

	elif request.method == 'POST' :
		serializer = EnfantCompleteSerializer(data = request.data, many = True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#non utilisé pour l'instant mais peut être utile pour effectuer des opérations sur un seul enfant à partir d'un format json.(EnfantComplete)
@api_view(['GET','PUT','DELETE'])
def detailsComplete(request, Nindiv):

	try :
		enfantComplete = EnfantComplete.objects.get(Nindiv = Nindiv)
	except Enfant.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = EnfantCompleteSerializer(enfantComplete)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = EnfantCompleteSerializer(enfant, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		enfantComplete.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
