# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0048_auto_20160526_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enfant',
            options={},
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='uuid',
        ),
        migrations.AddField(
            model_name='enfant',
            name='Nindiv',
            field=models.CharField(default=b'', max_length=100, db_index=True, blank=True),
        ),
    ]
