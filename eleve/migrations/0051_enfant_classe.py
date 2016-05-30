# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0050_remove_enfant_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='classe',
            field=models.CharField(default=b'', max_length=3, db_index=True, blank=True),
        ),
    ]
