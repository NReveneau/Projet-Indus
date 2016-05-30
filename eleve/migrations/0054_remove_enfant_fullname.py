# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0053_enfant_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='fullname',
        ),
    ]
