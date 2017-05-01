# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0019_registrationform_invoice_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='Payment_Method',
            field=models.BooleanField(default=False, help_text=b'<em>Please specify your payment method. <b> Note: Paypal payments include a 3.00% paypal fee, applied to the total amount owed.<b> <em><br><br>', choices=[(True, b'Online - Paypal'), (False, b'Cheque by Mail')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Cell_Phone',
            field=models.CharField(help_text=b'<br><br>', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Media_Consent',
            field=models.BooleanField(default=True, help_text=b'<h6><em>Every year, we hire photographers to capture every moment of SSUNS when it comes to the experience of the staffers, delegates and faculty advisors alike. In an effort to promote our conference, we would like to use these pictures on our website/brochure/pamphlets for others to see and learn more about SSUNS. Would your school be amenable for SSUNS to use such photos?</em></h6>', choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
