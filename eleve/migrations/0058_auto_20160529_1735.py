# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0057_enfant_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='date',
            field=models.DateField(default=None, null=True, verbose_name='date', blank=True),
        ),
    ]
