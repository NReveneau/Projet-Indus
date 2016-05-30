# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0032_auto_20160524_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='contact',
        ),
    ]
