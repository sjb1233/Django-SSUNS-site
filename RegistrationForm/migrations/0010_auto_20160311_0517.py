# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0009_auto_20160311_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Country',
            field=django_countries.fields.CountryField(default=b'Canada', max_length=2),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Fax',
            field=models.CharField(help_text=b'<p><h1>Committee Preferences (Please select 5)</h1></p>', max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Phone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Head_Delegate_Email',
            field=models.EmailField(default=b'', help_text=b'<br><em>Please enter a unique email address.</em><br><h2>Mailing Address</h2><p><em>Please enter the mailing address of your instituiton</em></p>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Will_this_be_your_first_time_attending_SSUNS',
            field=models.BooleanField(default=True, help_text=b'<p><h1>Contact Details</h1></p>', choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
