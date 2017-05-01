# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0037_auto_20161003_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='Crises',
            field=multiselectfield.db.fields.MultiSelectField(default=b'AD HOC', max_length=239, choices=[(b'AD HOC', b'AD HOC'), (b'FIRST ITALO-ETHIOPIAN WAR 1895-1896', b'FIRST ITALO-ETHIOPIAN WAR 1895-1896'), (b'RUSSO-JAPANESE WAR: RUSSIA', b'RUSSO-JAPANESE WAR: RUSSIA'), (b'RUSSO-JAPANESE WAR: JAPAN', b'RUSSO-JAPANESE WAR: JAPAN'), (b'LITERARY COMMITTEE ON ANIMAL FARM', b'LITERARY COMMITTEE ON ANIMAL FARM'), (b'MOUNT OLYMPUS', b'MOUNT OLYMPUS'), (b'NORTHWEST REBELLION', b'NORTHWEST REBELLION'), (b'POKEMON', b'POKEMON'), (b'POLISH-LITHUANIAN TEUTONIC WAR', b'POLISH-LITHUANIAN TEUTONIC WAR'), (b'UNITED NATIONS SECURITY COUNCIL 1961', b'UNITED NATIONS SECURITY COUNCIL 1961')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Faculty_Advisor_Email',
            field=models.EmailField(help_text=b'<i><small><small>Please enter a unique email address. The registration invoice will be sent to this email.</small></small></i>', max_length=254),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='General_Assemblies_and_ECOSOC',
            field=multiselectfield.db.fields.MultiSelectField(default=b'WORLD WATER FORUM', max_length=262, choices=[(b'WORLD WATER FORUM', b'WORLD WATER FORUM'), (b'SPECIAL POLITICAL AND DECOLONIZATION COMMITTEE', b'SPECIAL POLITICAL AND DECOLONIZATION COMMITTEE'), (b'UNITED NATIONS GENERAL ASSEMBLY REFUGEES AND MIGRANTS', b'UNITED NATIONS GENERAL ASSEMBLY REFUGEES AND MIGRANTS'), (b'WTO 2001', b'WTO 2001'), (b'COMMISSION ON SCIENCE AND TECHNOLOGY', b'COMMISSION ON SCIENCE AND TECHNOLOGY'), (b'UNITED NATIONS LATIN AMERICA', b'UNITED NATIONS LATIN AMERICA'), (b'UNITED NATIONS ENVIRONMENT PROGRAMME', b'UNITED NATIONS ENVIRONMENT PROGRAMME'), (b'UNITED NATIONS CRIME PREVENTION', b'UNITED NATIONS CRIME PREVENTION')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Number_of_Delegates',
            field=models.IntegerField(default=1, help_text=b"<em><small><small>There must be between 1 and 50 (inclusive) delegates. If you desire more delegates, email the Chargee d'Affaires.<b>Total is the sum of the delegation fee and per-delegate fee. NOTE: Schools located in Canada pay in CAD, and schools located in the United States and abroad pay in USD</b></em></small></small>", choices=[(1, b'Number of Delegates: 1 --- Total: $170.00'), (2, b'Number of Delegates: 2 --- Total: $255.00'), (3, b'Number of Delegates: 3 --- Total: $340.00'), (4, b'Number of Delegates: 4 --- Total: $425.00'), (5, b'Number of Delegates: 5 --- Total: $510.00'), (6, b'Number of Delegates: 6 --- Total: $595.00'), (7, b'Number of Delegates: 7 --- Total: $680.00'), (8, b'Number of Delegates: 8 --- Total: $765.00'), (9, b'Number of Delegates: 9 --- Total: $850.00'), (10, b'Number of Delegates: 10 --- Total: $935.00'), (11, b'Number of Delegates: 11 --- Total: $1020.00'), (12, b'Number of Delegates: 12 --- Total: $1105.00'), (13, b'Number of Delegates: 13 --- Total: $1190.00'), (14, b'Number of Delegates: 14 --- Total: $1275.00'), (15, b'Number of Delegates: 15 --- Total: $1360.00'), (16, b'Number of Delegates: 16 --- Total: $1445.00'), (17, b'Number of Delegates: 17 --- Total: $1530.00'), (18, b'Number of Delegates: 18 --- Total: $1615.00'), (19, b'Number of Delegates: 19 --- Total: $1700.00'), (20, b'Number of Delegates: 20 --- Total: $1785.00'), (21, b'Number of Delegates: 21 --- Total: $1870.00'), (22, b'Number of Delegates: 22 --- Total: $1955.00'), (23, b'Number of Delegates: 23 --- Total: $2040.00'), (24, b'Number of Delegates: 24 --- Total: $2125.00'), (25, b'Number of Delegates: 25 --- Total: $2210.00'), (26, b'Number of Delegates: 26 --- Total: $2295.00'), (27, b'Number of Delegates: 27 --- Total: $2380.00'), (28, b'Number of Delegates: 28 --- Total: $2465.00'), (29, b'Number of Delegates: 29 --- Total: $2550.00'), (30, b'Number of Delegates: 30 --- Total: $2635.00'), (31, b'Number of Delegates: 31 --- Total: $2720.00'), (32, b'Number of Delegates: 32 --- Total: $2805.00'), (33, b'Number of Delegates: 33 --- Total: $2890.00'), (34, b'Number of Delegates: 34 --- Total: $2975.00'), (35, b'Number of Delegates: 35 --- Total: $3060.00'), (36, b'Number of Delegates: 36 --- Total: $3145.00'), (37, b'Number of Delegates: 37 --- Total: $3230.00'), (38, b'Number of Delegates: 38 --- Total: $3315.00'), (39, b'Number of Delegates: 39 --- Total: $3400.00'), (40, b'Number of Delegates: 40 --- Total: $3485.00'), (41, b'Number of Delegates: 41 --- Total: $3570.00'), (42, b'Number of Delegates: 42 --- Total: $3655.00'), (43, b'Number of Delegates: 43 --- Total: $3740.00'), (44, b'Number of Delegates: 44 --- Total: $3825.00'), (45, b'Number of Delegates: 45 --- Total: $3910.00'), (46, b'Number of Delegates: 46 --- Total: $3995.00'), (47, b'Number of Delegates: 47 --- Total: $4080.00'), (48, b'Number of Delegates: 48 --- Total: $4165.00'), (49, b'Number of Delegates: 49 --- Total: $4250.00'), (50, b'Number of Delegates: 50 --- Total: $4335.00')]),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Previous_Model_UN_Experience',
            field=models.TextField(help_text=b"<i><small><small>Please describe your delegation's previous Model United Nations experiences, including past attendance/performance at SSUNS (if applicable), attendance/performance at other Model United Nations conferences, and any conferences organized by your delegation or school. If you wish, you may include this information in a separate e-mail addressed to Charge d'Affaires (schools@ssuns.org).</small></small></i>", null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Specialized_Agencies',
            field=multiselectfield.db.fields.MultiSelectField(default=b'ARAB LEAGUE 2011', max_length=266, choices=[(b'ARAB LEAGUE 2011', b'ARAB LEAGUE 2011'), (b'HUNGARIAN REVOLUTION', b'HUNGARIAN REVOLUTION'), (b'INTERNATIONAL CIVIL AVIATION ORGANIZATION 2001-2002', b'INTERNATIONAL CIVIL AVIATION ORGANIZATION 2001-2002'), (b'INTERNATIONAL COURT OF JUSTICE', b'INTERNATIONAL COURT OF JUSTICE'), (b'ISTHMIAN CANAL COMMISSION 1903-1904', b'ISTHMIAN CANAL COMMISSION 1903-1904'), (b'MYANMAR CONSTITUTIONAL ASSEMBLY', b'MYANMAR CONSTITUTIONAL ASSEMBLY'), (b"NATIVE WOMEN'S ASSOCIATION OF CANADA", b"NATIVE WOMEN'S ASSOCIATION OF CANADA"), (b'PARALYMPIC COMMITTEE', b'PARALYMPIC COMMITTEE'), (b'PEACE OF WESTPHALIA', b'PEACE OF WESTPHALIA')]),
        ),
    ]
