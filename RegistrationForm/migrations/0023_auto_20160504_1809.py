# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0022_auto_20160503_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='Cell_Phone_of_Head_Delegate',
            field=models.CharField(help_text=b'<em><small><small>This field is not required, but it is helpful to be able to contact a delegate if the faculty advisor is unavailable.</em></small></small>', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Alternate_Email',
            field=models.EmailField(default=b'', help_text=b'<em><small><small>Please enter a unique personal email address.</small></small></em>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Email',
            field=models.EmailField(help_text=b'<i><small><small>Please enter a unique email address. The registration response will be sent to this email.</small></small></i>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Name',
            field=models.CharField(help_text=b'<em><small><small>Please enter your first and last name</small></small></em>', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Fax',
            field=models.CharField(help_text=b'<p><br><h4>Committee Preferences (Max 3 per Category)</h4></p>', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Head_Delegate_Email',
            field=models.EmailField(default=b'', help_text=b'<em><small><small>Please enter a unique email address.</small></small></em><p><br><h4>Mailing Address</h4></p><p><em>Please enter the mailing address of your instituiton</em></p>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Head_Delegate_Name',
            field=models.CharField(help_text=b"<em><small><small>Please enter the head delegate's first and last name</small></small></em>", max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Media_Consent',
            field=models.BooleanField(default=True, help_text=b'<small><small><em>Every year, we hire photographers to capture every moment of SSUNS when it comes to the experience of the staffers, delegates and faculty advisors alike. In an effort to promote our conference, we would like to use these pictures on our website/brochure/pamphlets for others to see and learn more about SSUNS. Would your school be amenable for SSUNS to use such photos?</em></small></small>', choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Name_of_School',
            field=models.CharField(help_text=b'<em><small><small>Please enter the name of your institution</small></small></em>', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Number_of_Delegates',
            field=models.IntegerField(default=1, help_text=b"<em><small><small>There must be between 1 and 50 (inclusive) delegates. If you desire more delegates, email the Chargee d'Affaires.<b>Total is the sum of the delegation fee and per-delegate fee.</b></em></small></small>", choices=[(1, b'Number of Delegates: 1 --- Total: $180.00'), (2, b'Number of Delegates: 2 --- Total: $270.00'), (3, b'Number of Delegates: 3 --- Total: $360.00'), (4, b'Number of Delegates: 4 --- Total: $450.00'), (5, b'Number of Delegates: 5 --- Total: $540.00'), (6, b'Number of Delegates: 6 --- Total: $630.00'), (7, b'Number of Delegates: 7 --- Total: $720.00'), (8, b'Number of Delegates: 8 --- Total: $810.00'), (9, b'Number of Delegates: 9 --- Total: $900.00'), (10, b'Number of Delegates: 10 --- Total: $990.00'), (11, b'Number of Delegates: 11 --- Total: $1080.00'), (12, b'Number of Delegates: 12 --- Total: $1170.00'), (13, b'Number of Delegates: 13 --- Total: $1260.00'), (14, b'Number of Delegates: 14 --- Total: $1350.00'), (15, b'Number of Delegates: 15 --- Total: $1440.00'), (16, b'Number of Delegates: 16 --- Total: $1530.00'), (17, b'Number of Delegates: 17 --- Total: $1620.00'), (18, b'Number of Delegates: 18 --- Total: $1710.00'), (19, b'Number of Delegates: 19 --- Total: $1800.00'), (20, b'Number of Delegates: 20 --- Total: $1890.00'), (21, b'Number of Delegates: 21 --- Total: $1980.00'), (22, b'Number of Delegates: 22 --- Total: $2070.00'), (23, b'Number of Delegates: 23 --- Total: $2160.00'), (24, b'Number of Delegates: 24 --- Total: $2250.00'), (25, b'Number of Delegates: 25 --- Total: $2340.00'), (26, b'Number of Delegates: 26 --- Total: $2430.00'), (27, b'Number of Delegates: 27 --- Total: $2520.00'), (28, b'Number of Delegates: 28 --- Total: $2610.00'), (29, b'Number of Delegates: 29 --- Total: $2700.00'), (30, b'Number of Delegates: 30 --- Total: $2790.00'), (31, b'Number of Delegates: 31 --- Total: $2880.00'), (32, b'Number of Delegates: 32 --- Total: $2970.00'), (33, b'Number of Delegates: 33 --- Total: $3060.00'), (34, b'Number of Delegates: 34 --- Total: $3150.00'), (35, b'Number of Delegates: 35 --- Total: $3240.00'), (36, b'Number of Delegates: 36 --- Total: $3330.00'), (37, b'Number of Delegates: 37 --- Total: $3420.00'), (38, b'Number of Delegates: 38 --- Total: $3510.00'), (39, b'Number of Delegates: 39 --- Total: $3600.00'), (40, b'Number of Delegates: 40 --- Total: $3690.00'), (41, b'Number of Delegates: 41 --- Total: $3780.00'), (42, b'Number of Delegates: 42 --- Total: $3870.00'), (43, b'Number of Delegates: 43 --- Total: $3960.00'), (44, b'Number of Delegates: 44 --- Total: $4050.00'), (45, b'Number of Delegates: 45 --- Total: $4140.00'), (46, b'Number of Delegates: 46 --- Total: $4230.00'), (47, b'Number of Delegates: 47 --- Total: $4320.00'), (48, b'Number of Delegates: 48 --- Total: $4410.00'), (49, b'Number of Delegates: 49 --- Total: $4500.00'), (50, b'Number of Delegates: 50 --- Total: $4590.00')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Payment_Method',
            field=models.BooleanField(default=False, help_text=b'<em><small><small>Please specify your payment method. <b> Note: Paypal payments include a 3.00% paypal fee, applied to the total amount owed.</b> </em></small></small><br><br>', choices=[(True, b'Online - Paypal'), (False, b'Cheque by Mail')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Previous_Model_UN_Experience',
            field=models.TextField(help_text=b"<i><small><small>Please describe your delegation's previous Model United Nations experiences, including past attendance/performance at SSUNS (if applicable), attendance/performance at other Model United Nations conferences, and any conferences organized by your delegation or school. If you wish, you may include this information in a separate e-mail addressed to Wendy Zhang, Charge d'Affaires (schools@ssuns.org).</small></small></i>", null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Will_this_be_your_first_time_attending_SSUNS',
            field=models.BooleanField(default=True, help_text=b'<p><br><h4>Contact Details</h4></p>', choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]