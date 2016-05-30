# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0018_remove_entity_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.ForeignKey(to='Crm.Contact')),
            ],
        ),
    ]
