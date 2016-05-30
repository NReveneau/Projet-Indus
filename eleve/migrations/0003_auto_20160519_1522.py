# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0002_enfant_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='classe',
            field=models.ForeignKey(to='Crm.Group'),
        ),
    ]
