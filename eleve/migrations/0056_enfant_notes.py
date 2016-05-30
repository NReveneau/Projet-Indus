# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0055_remove_enfant_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'notes', blank=True),
        ),
    ]
