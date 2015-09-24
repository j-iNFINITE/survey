# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='isbaobei',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='answers',
            name='iscredit',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='answers',
            name='iszong',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='answers',
            name='most',
            field=models.IntegerField(null=True),
        ),
    ]
