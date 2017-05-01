# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0012_auto_20160317_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='GA',
            new_name='General_Assemblies_and_ECOSOC',
        ),
        migrations.RenameField(
            model_name='registrationform',
            old_name='Province_State_Region',
            new_name='Province_or_State_or_Region',
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Crises',
            field=multiselectfield.db.fields.MultiSelectField(default=b'Committee', max_length=53, choices=[(b'Committee', b'Committee'), (b'Committee2', b'Committee2'), (b'Committee3', b'Committee3'), (b'Committee4', b'Committee4'), (b'Committee5', b'Committee5')]),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Specialized_Agencies',
            field=multiselectfield.db.fields.MultiSelectField(default=b'Committee', max_length=53, choices=[(b'Committee', b'Committee'), (b'Committee2', b'Committee2'), (b'Committee3', b'Committee3'), (b'Committee4', b'Committee4'), (b'Committee5', b'Committee5')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Fax',
            field=models.CharField(help_text=b'<p><br><h2>Committee Preferences (Select up to 3 per Category)</h2></p>', max_length=30, null=True, blank=True),
        ),
    ]
