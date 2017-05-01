# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='advisor_name',
            new_name='full_name',
        ),
    ]
