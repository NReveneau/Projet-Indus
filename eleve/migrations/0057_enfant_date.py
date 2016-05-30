# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0056_enfant_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
