# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20150924_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='isdone',
            field=models.NullBooleanField(),
        ),
    ]
