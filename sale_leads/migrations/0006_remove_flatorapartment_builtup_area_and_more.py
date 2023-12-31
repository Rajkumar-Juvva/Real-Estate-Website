# Generated by Django 4.1.8 on 2023-04-30 12:22

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_leads', '0005_flatorapartment_property_utility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatorapartment',
            name='builtup_area',
        ),
        migrations.RemoveField(
            model_name='flatorapartment',
            name='carpet_area',
        ),
        migrations.RemoveField(
            model_name='flatorapartment',
            name='floor',
        ),
        migrations.AddField(
            model_name='flatorapartment',
            name='builtup_area_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Built-up Area Max'),
        ),
        migrations.AddField(
            model_name='flatorapartment',
            name='builtup_area_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Built-up Area Min'),
        ),
        migrations.AddField(
            model_name='flatorapartment',
            name='carpet_area_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Carpet Area Max'),
        ),
        migrations.AddField(
            model_name='flatorapartment',
            name='carpet_area_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Carpet Area Min'),
        ),
        migrations.AddField(
            model_name='flatorapartment',
            name='floor_max',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'), (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), (100, '100'), (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), (106, '106'), (107, '107'), (108, '108'), (109, '109'), (110, '110'), (111, '111'), (112, '112'), (113, '113'), (114, '114'), (115, '115'), (116, '116'), (117, '117'), (118, '118'), (119, '119'), (120, '120'), (121, '121'), (122, '122'), (123, '123'), (124, '124'), (125, '125'), (126, '126'), (127, '127'), (128, '128'), (129, '129'), (130, '130'), (131, '131'), (132, '132'), (133, '133'), (134, '134'), (135, '135'), (136, '136'), (137, '137'), (138, '138'), (139, '139'), (140, '140'), (141, '141'), (142, '142'), (143, '143'), (144, '144'), (145, '145'), (146, '146'), (147, '147'), (148, '148'), (149, '149'), (150, '150')], null=True, verbose_name='Floor Max'),
        ),
        migrations.AddField(
            model_name='flatorapartment',
            name='floor_min',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'), (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), (100, '100'), (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), (106, '106'), (107, '107'), (108, '108'), (109, '109'), (110, '110'), (111, '111'), (112, '112'), (113, '113'), (114, '114'), (115, '115'), (116, '116'), (117, '117'), (118, '118'), (119, '119'), (120, '120'), (121, '121'), (122, '122'), (123, '123'), (124, '124'), (125, '125'), (126, '126'), (127, '127'), (128, '128'), (129, '129'), (130, '130'), (131, '131'), (132, '132'), (133, '133'), (134, '134'), (135, '135'), (136, '136'), (137, '137'), (138, '138'), (139, '139'), (140, '140'), (141, '141'), (142, '142'), (143, '143'), (144, '144'), (145, '145'), (146, '146'), (147, '147'), (148, '148'), (149, '149'), (150, '150')], null=True, verbose_name='Floor Min'),
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='contact_id',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'mr Raj Kumar '), (2, 'Shiva '), (3, 'Rajesh '), (5, 'Mahesh '), (6, 'Salman Bhai '), (10, 'hello '), (4, 'Mallesh '), (11, 'Mars '), (12, 'elon '), (13, 'Jeff '), (7, 'I am ')], max_length=25, null=True, verbose_name='Contact Id'),
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='interiors',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Empty', 'Empty / Unfurnished'), ('Semi', 'Semi Furnished'), ('Fully', 'Fully Furnished')], max_length=10, null=True, verbose_name='Interiors'),
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='kitchen',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Empty', 'Empty'), ('Shelves', 'Shelves'), ('Modular', 'Modular')], max_length=10, null=True, verbose_name='Kitchen'),
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='property_utility',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Agricultural', 'Agricultural'), ('Commercial', 'Commercial'), ('Educational', 'Educational'), ('Hospital', 'Hospital'), ('Industrial', 'Industrial'), ('Lodging / Hotel', 'Lodging / Hotel'), ('Recreational', 'Recreational'), ('Residential', 'Residential'), ('Restaurant / Dinner', 'Restaurant / Dinner')], max_length=116, null=True, verbose_name='Property Utility'),
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='vastu_exit',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('East', 'East'), ('West', 'West'), ('North', 'North'), ('South', 'South')], max_length=5, null=True, verbose_name='Vastu / Exit'),
        ),
    ]
