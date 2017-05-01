# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0011_auto_20160311_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='GA',
            field=multiselectfield.db.fields.MultiSelectField(default=b'Committee', max_length=53, choices=[(b'Committee', b'Committee'), (b'Committee2', b'Committee2'), (b'Committee3', b'Committee3'), (b'Committee4', b'Committee4'), (b'Committee5', b'Committee5')]),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Previous_Model_UN_Experience',
            field=models.TextField(help_text=b"<h6><em>Please describe your delegation's previous Model United Nations experiences, including past attendance/performance at SSUNS (if applicable), attendance/performance at other Model United Nations conferences, and any conferences organized by your delegation or school. If you wish, you may include this information in a separate e-mail addressed to Koray Demir, Charge d'Affaires (schools@ssuns.org).</em></h6>", null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Address_Line_2',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Alternate_Email',
            field=models.EmailField(default=b'', help_text=b'<em>Please enter a unique personal email address.</em>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Email',
            field=models.EmailField(help_text=b'<em>Please enter a unique email address. The registration response will be sent to this email.</em>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Name',
            field=models.CharField(help_text=b'<em>Please enter your first and last name</em>', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Fax',
            field=models.CharField(help_text=b'<p><br><h2>Committee Preferences (Please select 5)</h2></p>', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Head_Delegate_Email',
            field=models.EmailField(default=b'', help_text=b'<em>Please enter a unique email address.</em><p><br><h1>Mailing Address</h1></p><p><em>Please enter the mailing address of your instituiton</em></p>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Head_Delegate_Name',
            field=models.CharField(help_text=b"<em>Please enter the head delegate's first and last name</em>", max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Name_of_School',
            field=models.CharField(help_text=b'<em>Please enter the name of your institution</em>', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Number_of_Delegates',
            field=models.IntegerField(default=1, help_text=b"<em>There must be between 1 and 50 (inclusive) delegates. If you desire more delegates, email the Chargee d'Affaires.</em>", validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Will_this_be_your_first_time_attending_SSUNS',
            field=models.BooleanField(default=True, help_text=b'<p><br><h1>Contact Details</h1></p>', choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
