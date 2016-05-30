# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0027_remove_enfant_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='gender',
            field=models.IntegerField(default=0, blank=True, verbose_name='gender', choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Mrs and Mr')]),
        ),
    ]
