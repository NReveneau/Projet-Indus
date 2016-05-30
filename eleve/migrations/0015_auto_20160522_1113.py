# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import balafon.Crm.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0018_remove_entity_student'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eleve', '0014_enfant_lastname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enfant',
            options={'ordering': ('lastname', 'firstname'), 'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AddField(
            model_name='enfant',
            name='accept_notifications',
            field=models.BooleanField(default=True, help_text='We may have to notify you some events (e.g. a new message).', verbose_name=b'accept notifications'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='address', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='address2',
            field=models.CharField(default='', max_length=200, verbose_name='address 2', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='address3',
            field=models.CharField(default='', max_length=200, verbose_name='address 3', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_address',
            field=models.CharField(default='', max_length=200, verbose_name='address', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_address2',
            field=models.CharField(default='', max_length=200, verbose_name='address 2', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_address3',
            field=models.CharField(default='', max_length=200, verbose_name='address 3', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_cedex',
            field=models.CharField(default='', max_length=200, verbose_name='cedex', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_city',
            field=models.ForeignKey(related_name='enfant_billing_set', default=None, blank=True, to='Crm.City', null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_street_number',
            field=models.CharField(default=b'', max_length=20, verbose_name='street number', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_street_type',
            field=models.ForeignKey(related_name='enfant_billing_set', default=None, blank=True, to='Crm.StreetType', null=True, verbose_name='street type'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='billing_zip_code',
            field=models.CharField(default='', max_length=20, verbose_name='zip code', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='birth_date',
            field=models.DateField(default=None, null=True, verbose_name='birth date', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='cedex',
            field=models.CharField(default='', max_length=200, verbose_name='cedex', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='city',
            field=models.ForeignKey(default=None, blank=True, to='Crm.City', null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(default=None, verbose_name='created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enfant',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name=b'email', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name=b'email verified'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='entity',
            field=models.ForeignKey(default=None, to='Crm.Entity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enfant',
            name='favorite_language',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'favorite language', blank=True, choices=[(b'', 'Par d\xe9faut'), (b'fr', 'Fran\xe7ais'), (b'en', 'English')]),
        ),
        migrations.AddField(
            model_name='enfant',
            name='gender',
            field=models.IntegerField(default=0, blank=True, verbose_name='gender', choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Mrs and Mr')]),
        ),
        migrations.AddField(
            model_name='enfant',
            name='has_left',
            field=models.BooleanField(default=False, verbose_name='has left'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='job',
            field=models.CharField(default='', max_length=200, verbose_name='job', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='last_modified_by',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='main_contact',
            field=models.BooleanField(default=True, db_index=True, verbose_name=b'main contact'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='mobile',
            field=models.CharField(default='', max_length=200, verbose_name=b'mobile', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(default=None, verbose_name='modified', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enfant',
            name='nickname',
            field=models.CharField(default='', max_length=200, verbose_name='nickname', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'notes', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='phone',
            field=models.CharField(default='', max_length=200, verbose_name=b'phone', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='photo',
            field=models.ImageField(default='', upload_to=balafon.Crm.models.get_contact_photo_dir, verbose_name='photo', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='role',
            field=models.ManyToManyField(default=None, to='Crm.EntityRole', verbose_name='Roles', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='same_as',
            field=models.ForeignKey(default=None, blank=True, to='Crm.SameAs', null=True, verbose_name='same as'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='same_as_priority',
            field=models.IntegerField(default=0, verbose_name='same as priority'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='street_number',
            field=models.CharField(default=b'', max_length=20, verbose_name='street number', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='street_type',
            field=models.ForeignKey(default=None, blank=True, to='Crm.StreetType', null=True, verbose_name='street type'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='title', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='uuid',
            field=models.CharField(default=b'', max_length=100, db_index=True, blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='zip_code',
            field=models.CharField(default='', max_length=20, verbose_name='zip code', blank=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='firstname',
            field=models.CharField(default='', max_length=200, verbose_name='first name', blank=True),
        ),
    ]
