# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0006_auto_20160310_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='WillthisbeyourfirsttimeattendingSSUNS',
            new_name='Will_this_be_your_first_time_attending_SSUNS',
        ),
    ]
