# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0031_auto_20160524_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='E1',
            field=models.TimeField(default=None, null=True, verbose_name='E1', blank=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='E2',
            field=models.TimeField(default=None, null=True, verbose_name='E2', blank=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='S1',
            field=models.TimeField(default=None, null=True, verbose_name='S1', blank=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='S2',
            field=models.TimeField(default=None, null=True, verbose_name='S2', blank=True),
        ),
    ]
