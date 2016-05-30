# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0018_remove_entity_student'),
        ('eleve', '0019_enfant_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='entity',
        ),
        migrations.AddField(
            model_name='enfant',
            name='classe',
            field=models.ForeignKey(default=None, to='Crm.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enfant',
            name='contact',
            field=models.ForeignKey(default=None, to='Crm.Contact'),
            preserve_default=False,
        ),
    ]
