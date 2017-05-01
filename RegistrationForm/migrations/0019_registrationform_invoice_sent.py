# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0018_auto_20160326_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Invoice_Sent',
            field=models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
