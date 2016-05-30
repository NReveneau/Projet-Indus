# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0030_remove_enfant_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='E1',
            field=models.DateField(default=None, null=True, verbose_name='birth date', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='E2',
            field=models.DateField(default=None, null=True, verbose_name='birth date', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='S1',
            field=models.DateField(default=None, null=True, verbose_name='birth date', blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='S2',
            field=models.DateField(default=None, null=True, verbose_name='birth date', blank=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='contact',
            field=models.ForeignKey(default=None, to='Crm.Contact'),
        ),
    ]
