# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0015_auto_20160522_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='accept_notifications',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='email_verified',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='favorite_language',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='has_left',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='job',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='main_contact',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='role',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='same_as',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='same_as_priority',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='title',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='uuid',
        ),
    ]
