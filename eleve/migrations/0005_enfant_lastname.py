# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0004_auto_20160519_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='lastname',
            field=models.CharField(default='', max_length=200, verbose_name='last name', db_index=True, blank=True),
        ),
    ]
