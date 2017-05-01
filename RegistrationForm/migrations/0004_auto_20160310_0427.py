# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0003_registrationform_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='full_name',
            new_name='Faculty_Advisor_Name',
        ),
        migrations.RenameField(
            model_name='registrationform',
            old_name='school_name',
            new_name='Name_of_School',
        ),
    ]
