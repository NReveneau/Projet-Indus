# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0007_auto_20160519_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='Classe',
            field=models.CharField(default='', max_length=200, verbose_name='classe', db_index=True, blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='firstname',
            field=models.CharField(default='', max_length=200, verbose_name='first name', db_index=True, blank=True),
        ),
    ]
