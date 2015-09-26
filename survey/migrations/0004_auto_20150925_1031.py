# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_answers_isdone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='iszong',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='most',
        ),
        migrations.AddField(
            model_name='answers',
            name='Q1_most',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='answers',
            name='Q2_choice',
            field=models.CharField(null=True, max_length=1),
        ),
        migrations.AddField(
            model_name='answers',
            name='Q2_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='Q3_choice',
            field=models.CharField(null=True, max_length=1),
        ),
        migrations.AddField(
            model_name='answers',
            name='Q3_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='Q_baobei',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='Q_iscredit',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='Q_overbank',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='islow',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='answers',
            name='isoverbank',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='answers',
            name='m_address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='m_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='m_phone',
            field=models.IntegerField(null=True),
        ),
    ]
