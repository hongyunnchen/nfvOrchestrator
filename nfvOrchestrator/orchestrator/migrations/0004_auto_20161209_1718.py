# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orchestrator', '0003_rsp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsp',
            old_name='sfNameList',
            new_name='rspResponse_json',
        ),
    ]