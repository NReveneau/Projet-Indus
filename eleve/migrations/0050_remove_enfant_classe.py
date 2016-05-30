# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0049_auto_20160529_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='classe',
        ),
    ]
