# -*- coding: utf-8 -*-
"""models"""
# pylint: disable=model-no-explicit-unicode


from django.db import models

#modèles contenant les informations nécessaires à la liaison avec l'application mobile
class Enfant(models.Model):

	nom = models.CharField((u'last name'), max_length=200, blank=False, default=u'', db_index=True)
	prenom = models.CharField((u'first name'), max_length=200, blank=False, default=u'')
	E1 = models.TimeField((u"E1"), blank=True, default=None, null=True)
	E2 = models.TimeField((u"E2"), blank=True, default=None, null=True)
	S1 = models.TimeField((u"S1"), blank=True, default=None, null=True)
	S2 = models.TimeField((u"S2"), blank=True, default=None, null=True)
	phone = models.CharField(('phone'), max_length=200, blank=True, default=u'')
	mobile = models.CharField(('mobile'), max_length=200, blank=True, default=u'')
	email = models.EmailField(('email'), blank=True, default=u'')	
	Nindiv = models.CharField(max_length=100, blank=True, default=None, db_index=True)	
	notes = models.TextField(('notes'), blank=True, default="")
	classe = models.CharField(max_length=3, blank=True, default=None, db_index=True)
	date = models.DateField(blank=True, default=None, null=False)
	age = models.CharField(('age'),max_length=2, blank = True, default=None,null=True) 


class EnfantComplete(models.Model):

	nom = models.CharField((u'last name'), max_length=200, blank=False, default=u'', db_index=True)
	prenom = models.CharField((u'first name'), max_length=200, blank=False, default=u'')
	E1 = models.TimeField((u"E1"), blank=False, default=None)
	E2 = models.TimeField((u"E2"), blank=False, default=None)
	S1 = models.TimeField((u"S1"), blank=False, default=None)
	S2 = models.TimeField((u"S2"), blank=False, default=None)
	phone = models.CharField(('phone'), max_length=200, blank=True, default=u'')
	mobile = models.CharField(('mobile'), max_length=200, blank=True, default=u'')
	email = models.EmailField(('email'), blank=True, default=u'')	
	Nindiv = models.CharField(max_length=100, blank=True, default=None, db_index=True)	
	notes = models.TextField(('notes'), blank=True, default="")
	classe = models.CharField(max_length=3, blank=True, default=None, db_index=True)
	date = models.DateField(blank=True, default=None, null=False)
	age = models.CharField(('age'),max_length=2, blank = True, default=None,null=True) 
