# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0013_auto_20160317_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Secretariate_Log',
            field=models.TextField(default=b'ex. BY SSUNS IT: This school changed from 9 dels to 10 dels', help_text=b'SSQUAD: Fill this out if you make any changes, yo!', null=True),
        ),
    ]
