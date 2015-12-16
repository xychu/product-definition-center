# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0008_auto_20151214_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='composeimagertttests',
            old_name='rtt_testing_status',
            new_name='test_result',
        ),
    ]
