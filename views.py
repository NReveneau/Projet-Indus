from django.shortcuts import render
from django.shortcuts import redirect
from forms import *
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, date



def enfant_list(request):
	enfants=Enfant.objects.all()
	return render(request,'appli/enfant_liste.html',{'enfants': enfants})

def enfantcomplete_list(request):
	enfantscomplete=EnfantComplete.objects.all()
	return render(request,'appli/enfantcomplete_liste.html',{'enfantscomplete': enfantscomplete})

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
