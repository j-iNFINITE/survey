# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('SN', models.CharField(serialize=False, max_length=18, primary_key=True)),
                ('iszong', models.BooleanField()),
                ('iscredit', models.BooleanField()),
                ('isbaobei', models.BooleanField()),
                ('most', models.IntegerField()),
            ],
        ),
    ]
