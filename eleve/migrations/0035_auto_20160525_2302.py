# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0034_enfant_entity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='entity',
        ),
        migrations.AddField(
            model_name='enfant',
            name='classe',
            field=models.CharField(default='', max_length=3, verbose_name='classe', blank=True),
        ),
    ]
