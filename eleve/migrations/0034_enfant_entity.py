# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0018_remove_entity_student'),
        ('eleve', '0033_remove_enfant_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='entity',
            field=models.ForeignKey(default=None, to='Crm.Entity'),
            preserve_default=False,
        ),
    ]
