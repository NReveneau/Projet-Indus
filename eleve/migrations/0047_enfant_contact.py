# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0018_remove_entity_student'),
        ('eleve', '0046_auto_20160526_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='contact',
            field=models.ForeignKey(default=None, to='Crm.Contact'),
            preserve_default=False,
        ),
    ]
