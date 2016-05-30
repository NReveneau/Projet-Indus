# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0052_remove_enfant_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='fullname',
            field=models.CharField(default=b'firstnamelastname', max_length=400, blank=True),
        ),
    ]
