# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0015_auto_20160326_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='Cell_Phone',
            field=models.CharField(help_text=b'<br>', max_length=30, null=True),
        ),
    ]
