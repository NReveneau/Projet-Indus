# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0018_remove_entity_student'),
        ('eleve', '0008_auto_20160519_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='Classe',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='lastname',
        ),
        migrations.AddField(
            model_name='enfant',
            name='classe',
            field=models.ForeignKey(default='', to='Crm.Group'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='contact',
            field=models.ForeignKey(default='', to='Crm.Contact'),
        ),
    ]
