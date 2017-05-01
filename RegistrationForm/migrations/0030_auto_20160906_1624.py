# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0029_auto_20160904_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegateinput',
            name='Faculty_Advisor_1_Name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='delegateinput',
            name='Faculty_Advisor_2_Name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='delegateinput',
            name='Faculty_Advisor_3_Name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='delegateinput',
            name='Faculty_Advisor_4_Name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='delegateinput',
            name='Faculty_Advisor_5_Name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
