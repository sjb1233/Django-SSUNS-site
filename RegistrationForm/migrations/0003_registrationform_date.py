# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0002_auto_20160309_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 10, 3, 25, 0, 78910, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
