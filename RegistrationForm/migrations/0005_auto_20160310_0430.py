# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0004_auto_20160310_0427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='email',
            new_name='Faculty_Advisor_Email',
        ),
    ]
