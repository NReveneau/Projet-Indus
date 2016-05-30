# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0040_enfant_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='contact',
            field=models.ForeignKey(to='Crm.Contact'),
        ),
    ]
