# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0009_auto_20160519_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='contact',
            field=models.ForeignKey(default='Mr', to='Crm.Contact'),
        ),
    ]
