# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0017_auto_20160326_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Are_there_any_allergies_or_concerns_that_we_should_know_about',
            field=models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Media_Consent',
            field=models.BooleanField(default=True, help_text=b'<em>Every year, we hire photographers to capture every moment of SSUNS when it comes to the experience of the staffers, delegates and faculty advisors alike. In an effort to promote our conference, we would like to use these pictures on our website/brochure/pamphlets for others to see and learn more about SSUNS. Would your school be amenable for SSUNS to use such photos?</em>', choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='Please_Specify',
            field=models.TextField(null=True, blank=True),
        ),
    ]
