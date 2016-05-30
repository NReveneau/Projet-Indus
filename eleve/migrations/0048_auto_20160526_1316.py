# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0047_enfant_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enfant',
            old_name='numero',
            new_name='uuid',
        ),
    ]
