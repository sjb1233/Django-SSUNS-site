# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0020_auto_20160401_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='Number_of_Delegates',
            field=models.IntegerField(default=1, help_text=b"<em>There must be between 1 and 50 (inclusive) delegates. If you desire more delegates, email the Chargee d'Affaires.</em>", choices=[(1, b'Total: $170.00'), (2, b'Total: $255.00'), (3, b'Total: $340.00'), (4, b'Total: $425.00'), (5, b'Total: $510.00'), (6, b'Total: $595.00'), (7, b'Total: $680.00'), (8, b'Total: $765.00'), (9, b'Total: $850.00'), (10, b'Total: $935.00'), (11, b'Total: $1020.00'), (12, b'Total: $1105.00'), (13, b'Total: $1190.00'), (14, b'Total: $1275.00'), (15, b'Total: $1360.00'), (16, b'Total: $1445.00'), (17, b'Total: $1530.00'), (18, b'Total: $1615.00'), (19, b'Total: $1700.00'), (20, b'Total: $1785.00'), (21, b'Total: $1870.00'), (22, b'Total: $1955.00'), (23, b'Total: $2040.00'), (24, b'Total: $2125.00'), (25, b'Total: $2210.00'), (26, b'Total: $2295.00'), (27, b'Total: $2380.00'), (28, b'Total: $2465.00'), (29, b'Total: $2550.00'), (30, b'Total: $2635.00'), (31, b'Total: $2720.00'), (32, b'Total: $2805.00'), (33, b'Total: $2890.00'), (34, b'Total: $2975.00'), (35, b'Total: $3060.00'), (36, b'Total: $3145.00'), (37, b'Total: $3230.00'), (38, b'Total: $3315.00'), (39, b'Total: $3400.00'), (40, b'Total: $3485.00'), (41, b'Total: $3570.00'), (42, b'Total: $3655.00'), (43, b'Total: $3740.00'), (44, b'Total: $3825.00'), (45, b'Total: $3910.00'), (46, b'Total: $3995.00'), (47, b'Total: $4080.00'), (48, b'Total: $4165.00'), (49, b'Total: $4250.00'), (50, b'Total: $4335.00')]),
        ),
    ]
