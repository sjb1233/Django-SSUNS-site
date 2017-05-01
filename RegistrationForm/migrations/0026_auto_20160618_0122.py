# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0025_auto_20160527_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='Specialized_Agencies',
            field=multiselectfield.db.fields.MultiSelectField(default=b'Bilingual: Charlottetown Conference', max_length=349, choices=[(b'Bilingual: Canadian Confederation', b'Bilingual: Charlottetown Conference'), (b'National Football League 2016', b'National Football League 2016'), (b'Microsoft Board of Directors', b'Microsoft Board of Directors'), (b'International Atomic Energy Agency 2017', b'International Atomic Energy Agency 2017'), (b'Venezuelan National Assembly', b'Venezuelan National Assembly'), (b'8th United States Congress 1803', b'8th United States Congress 1803'), (b'Czechoslovak Government 1990', b'Czechoslovak Government 1990'), (b'United Nations Office for Outer Space Affairs and International Civil Aviation Organization - 3rd International Symposium 2017', b'United Nations Office for Outer Space Affairs and International Civil Aviation Organization - 3rd International Symposium 2017')]),
        ),
    ]
