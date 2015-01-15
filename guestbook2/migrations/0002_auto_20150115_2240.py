# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, null=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='website',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
    ]
