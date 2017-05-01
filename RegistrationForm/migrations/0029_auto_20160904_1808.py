# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0028_auto_20160802_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelegateInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name_of_School', models.CharField(help_text=b'<em><small><small>Please enter the name of your institution</small></small></em>', max_length=120, null=True)),
                ('Delegate_1', models.CharField(max_length=120, null=True)),
                ('Delegate_1_Country', models.CharField(max_length=120, null=True)),
                ('Delegate_1_Committee', models.CharField(max_length=120, null=True)),
                ('Delegate_2', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_2_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_2_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_3', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_3_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_3_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_4', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_4_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_4_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_5', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_5_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_5_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_6', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_6_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_6_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_7', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_7_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_7_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_8', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_8_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_8_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_9', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_9_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_9_Committee', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_10', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_10_Country', models.CharField(max_length=120, null=True, blank=True)),
                ('Delegate_10_Committee', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PositionPaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name_of_School', models.CharField(help_text=b'<em><small><small>Please enter the name of your institution</small></small></em>', max_length=120, null=True)),
                ('Your_Name', models.CharField(help_text=b'<em><small><small>Please enter your full name</small></small></em>', max_length=120, null=True)),
                ('Your_Committee', models.CharField(help_text=b'<em><small><small>Please enter the name of your committee</small></small></em>', max_length=120, null=True)),
                ('Your_Country', models.CharField(help_text=b'<em><small><small>Please enter the name of your country</small></small></em>', max_length=120, null=True)),
                ('file', models.FileField(null=True, upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Paid',
            field=models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
