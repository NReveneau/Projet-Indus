# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0038_remove_enfant_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='contact',
        ),
        migrations.AddField(
            model_name='enfant',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name=b'email', blank=True),
        ),
    ]
