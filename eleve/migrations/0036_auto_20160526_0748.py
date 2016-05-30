# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0035_auto_20160525_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='enfant',
            name='date',
            field=models.DateField(default=None, null=True, verbose_name='date', blank=True),
        ),
    ]
