# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0007_auto_20160310_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Faculty_Advisor_Alternate_Email',
            field=models.EmailField(default=b'', help_text=b'<br><em>Please enter a unique personal email address.</em>', max_length=254),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Head_Delegate_Name',
            field=models.CharField(help_text=b"<br><em>Please enter the head delegate's first and last name</em>", max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Email',
            field=models.EmailField(help_text=b'<br><em>Please enter a unique email address. The registration response will be sent to this email.</em>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Will_this_be_your_first_time_attending_SSUNS',
            field=models.BooleanField(default=True, help_text=b'<br><h1>Contact Details</h1>', choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
