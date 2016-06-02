# -*- coding: utf-8 -*-
"""models"""
# pylint: disable=model-no-explicit-unicode


from django.db import models

class Enfant(models.Model):
#La classe Enfant correspond à une séance: elle comprend donc la date, le nom de l'eleve, son numéro individuel, sa classe, ainsi que les pointages.
#Les champs de contact sont présents qi il y a besoin de contacter les parent a propos de la scéance pour une quelconque raison.


	lastname = models.CharField((u'last name'), max_length=200, blank=True, default=u'', db_index=True)
	firstname = models.CharField((u'first name'), max_length=200, blank=True, default=u'')
	Nindiv = models.CharField(max_length=100, blank=True, default='', db_index=True)
	classe = models.CharField(max_length=3, blank=True, default='', db_index=True)
	#Les champs E1 E2 S1 S2 correspondent aux heure d'arrivée de sortie de l'enfant
	E1 = models.TimeField((u"E1"), blank=True, default=None, null=True)
	E2 = models.TimeField((u"E2"), blank=True, default=None, null=True)
	S1 = models.TimeField((u"S1"), blank=True, default=None, null=True)
	S2 = models.TimeField((u"S2"), blank=True, default=None, null=True)
	date = models.DateField(blank=True, default=None, null=True)
	#Les champs de contact
	phone = models.CharField(('phone'), max_length=200, blank=True, default=u'')
	mobile = models.CharField(('mobile'), max_length=200, blank=True, default=u'')
	email = models.EmailField(('email'), blank=True, default=u'')
	notes = models.TextField(('notes'), blank=True, default="")
	classe = models.CharField(max_length=3, blank=True, default='', db_index=True)


	def __unicode__(self):
		return u"{0} {1}".format(self.firstname, self.lastname)
