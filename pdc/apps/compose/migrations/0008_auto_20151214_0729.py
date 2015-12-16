# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pdc.apps.compose.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150512_0703'),
        ('package', '0007_auto_20151208_1011'),
        ('compose', '0007_auto_20151120_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComposeImageRTTTests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arch', models.ForeignKey(to='common.Arch')),
                ('image', models.ForeignKey(to='package.Image')),
                ('rtt_testing_status', models.ForeignKey(default=pdc.apps.compose.models._get_untested, to='compose.ComposeAcceptanceTestingState')),
                ('variant', models.ForeignKey(to='compose.Variant')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='composeimagertttests',
            unique_together=set([('variant', 'arch', 'image')]),
        ),
    ]
