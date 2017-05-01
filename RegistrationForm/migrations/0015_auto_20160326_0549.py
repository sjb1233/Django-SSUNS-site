# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0014_registrationform_secretariate_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Cell_Phone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Cell_Phone_of_Head_Delegates',
            field=models.CharField(help_text=b'<em>This field is not required, but it is helpful to be able to get a hold of a delegate if the faculty advisor is unavailable.</em>', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Secretariate_Log',
            field=models.TextField(default=b'ex. BY SSUNS IT: This school changed from 9 dels to 10 dels', help_text=b'SSQUAD: Fill this out if you make any changes, yo!', null=True, blank=True),
        ),
    ]
