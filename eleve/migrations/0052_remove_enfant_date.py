# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0051_enfant_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='date',
        ),
    ]
