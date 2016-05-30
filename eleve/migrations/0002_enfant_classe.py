# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='classe',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
