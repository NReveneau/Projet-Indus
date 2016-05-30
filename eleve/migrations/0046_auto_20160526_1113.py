# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0045_remove_enfant_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enfant',
            old_name='uuid',
            new_name='numero',
        ),
    ]
