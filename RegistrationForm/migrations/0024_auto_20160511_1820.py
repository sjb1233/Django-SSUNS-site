# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0023_auto_20160504_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='Secretariate_Log',
            new_name='Secretariat_Log',
        ),
    ]
