# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0018_remove_entity_student'),
        ('eleve', '0028_enfant_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='classe',
            field=models.ForeignKey(default=None, to='Crm.Group'),
            preserve_default=False,
        ),
    ]
