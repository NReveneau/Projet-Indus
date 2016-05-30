# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0023_remove_enfant_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='address',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='address3',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_address2',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_address3',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_cedex',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_city',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_street_number',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_street_type',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='billing_zip_code',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='cedex',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='city',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='created',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='street_number',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='street_type',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='zip_code',
        ),
    ]
