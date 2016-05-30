# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0010_auto_20160519_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='classe',
        ),
        migrations.AddField(
            model_name='enfant',
            name='firstname',
            field=models.CharField(default='', max_length=200, verbose_name='first name', db_index=True, blank=True),
        ),
        migrations.AddField(
            model_name='enfant',
            name='lastname',
            field=models.CharField(default='', max_length=200, verbose_name='last name', db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='contact',
            field=models.ForeignKey(to='Crm.Contact'),
        ),
    ]
