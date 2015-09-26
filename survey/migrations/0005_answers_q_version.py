# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20150925_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='Q_version',
            field=models.TextField(null=True),
        ),
    ]
