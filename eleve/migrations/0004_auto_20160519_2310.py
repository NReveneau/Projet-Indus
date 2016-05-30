# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0003_auto_20160519_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='contact',
        ),
        migrations.AddField(
            model_name='enfant',
            name='text',
            field=models.TextField(default='', verbose_name='text'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='title'),
        ),
    ]
