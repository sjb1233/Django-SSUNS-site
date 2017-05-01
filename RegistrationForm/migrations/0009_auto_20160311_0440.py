# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0008_auto_20160310_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Address_Line_1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Address_Line_2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='City',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Head_Delegate_Email',
            field=models.EmailField(default=b'', help_text=b'<br><em>Please enter a unique email address.</em><br><h2>Mailing Address</h2>', max_length=254),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Province_State_Region',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
