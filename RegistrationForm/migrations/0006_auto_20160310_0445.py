# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0005_auto_20160310_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='WillthisbeyourfirsttimeattendingSSUNS',
            field=models.BooleanField(default=True, choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Email',
            field=models.EmailField(help_text=b'<br><em>Please enter an unique email address. The registration response will be sent to this email.</em>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Name',
            field=models.CharField(help_text=b'<br><em>Please enter your first and last name</em>', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Name_of_School',
            field=models.CharField(help_text=b'<br><em>Please enter the name of your institution</em>', max_length=120, null=True),
        ),
    ]
