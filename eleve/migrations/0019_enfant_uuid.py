# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0018_remove_enfant_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='uuid',
            field=models.CharField(default=b'', max_length=100, db_index=True, blank=True),
        ),
    ]
