# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0016_auto_20160326_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='Cell_Phone_of_Head_Delegates',
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Cell_Phone_of_Head_Delegate',
            field=models.CharField(help_text=b'<em>This field is not required, but it is helpful to be able to contact a delegate if the faculty advisor is unavailable.</em>', max_length=30, null=True, blank=True),
        ),
    ]
