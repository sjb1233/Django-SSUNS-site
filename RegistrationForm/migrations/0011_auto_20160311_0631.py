# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0010_auto_20160311_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Number_of_Delegates',
            field=models.IntegerField(default=1, help_text=b"<br><em>There must be between 1 and 50 (inclusive) delegates. If you desire more delegates, email the Chargee d'Affaires.", validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
