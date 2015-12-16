# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pdc.apps.compose.models


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0009_auto_20151214_0747'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='composeimagertttests',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='composeimagertttests',
            name='arch',
        ),
        migrations.RemoveField(
            model_name='composeimagertttests',
            name='image',
        ),
        migrations.RemoveField(
            model_name='composeimagertttests',
            name='test_result',
        ),
        migrations.RemoveField(
            model_name='composeimagertttests',
            name='variant',
        ),
        migrations.AddField(
            model_name='composeimage',
            name='rtt_test_result',
            field=models.ForeignKey(default=pdc.apps.compose.models._get_untested, to='compose.ComposeAcceptanceTestingState'),
        ),
        migrations.DeleteModel(
            name='ComposeImageRTTTests',
        ),
    ]
