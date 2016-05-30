# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0011_auto_20160519_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='lastname',
        ),
    ]
