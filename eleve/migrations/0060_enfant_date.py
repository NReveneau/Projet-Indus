# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0059_remove_enfant_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
