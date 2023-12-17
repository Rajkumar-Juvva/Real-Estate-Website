# Generated by Django 4.1.8 on 2023-05-09 14:02

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_inventory', '0006_alter_flatorapartment_contact_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleInventoryBungalow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[], max_length=200, null=True, verbose_name='Contact Id')),
                ('property_utility', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Agricultural', 'Agricultural'), ('Commercial', 'Commercial'), ('Educational', 'Educational'), ('Hospital', 'Hospital'), ('Industrial', 'Industrial'), ('Lodging / Hotel', 'Lodging / Hotel'), ('Recreational', 'Recreational'), ('Residential', 'Residential'), ('Restaurant / Dinner', 'Restaurant / Dinner')], max_length=116, null=True, verbose_name='Property Utility')),
                ('tags', models.TextField(blank=True, null=True, verbose_name='Tags')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('inventory_id', models.BigIntegerField(unique=True, verbose_name='Inventory Id')),
                ('created_by', models.IntegerField(null=True, verbose_name='Created By')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(null=True, verbose_name='Updated By')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('video_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Video Link')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('bedroom', models.CharField(blank=True, choices=[('1RK', '1RK'), ('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK'), ('5BHK', '5BHK'), ('6BHK', '6BHK'), ('7BHK', '7BHK'), ('8BHK', '8BHK'), ('9BHK', '9BHK'), ('10BHK', '10BHK')], max_length=5, null=True, verbose_name='Bedroom')),
                ('bathroom', models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True, verbose_name='Bathroom')),
                ('carpet_units', models.CharField(blank=True, choices=[('sq ft', 'sq ft'), ('sq mt', 'sq mt')], max_length=5, null=True, verbose_name='Carpet Units')),
                ('carpet_area', models.IntegerField(blank=True, null=True, verbose_name='Carpet Area')),
                ('builtup_units', models.CharField(blank=True, choices=[('sq ft', 'sq ft'), ('sq mt', 'sq mt')], max_length=5, null=True, verbose_name='Built-up Units')),
                ('builtup_area', models.IntegerField(blank=True, null=True, verbose_name='Built-up Area')),
                ('total_floor', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'), (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), (100, '100'), (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), (106, '106'), (107, '107'), (108, '108'), (109, '109'), (110, '110'), (111, '111'), (112, '112'), (113, '113'), (114, '114'), (115, '115'), (116, '116'), (117, '117'), (118, '118'), (119, '119'), (120, '120'), (121, '121'), (122, '122'), (123, '123'), (124, '124'), (125, '125'), (126, '126'), (127, '127'), (128, '128'), (129, '129'), (130, '130'), (131, '131'), (132, '132'), (133, '133'), (134, '134'), (135, '135'), (136, '136'), (137, '137'), (138, '138'), (139, '139'), (140, '140'), (141, '141'), (142, '142'), (143, '143'), (144, '144'), (145, '145'), (146, '146'), (147, '147'), (148, '148'), (149, '149'), (150, '150')], null=True, verbose_name='Total Floor')),
                ('open_space', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Terrace', 'Terrace'), ('Balcony', 'Balcony'), ('Deck', 'Deck'), ('Lawn', 'Lawn')], max_length=25, null=True, verbose_name='Open Space')),
                ('vastu_exit', models.CharField(blank=True, choices=[('East', 'East'), ('West', 'West'), ('North', 'North'), ('South', 'South')], max_length=5, null=True, verbose_name='Vastu / Exit')),
                ('interiors', models.CharField(blank=True, choices=[('Empty', 'Empty / Unfurnished'), ('Semi', 'Semi Furnished'), ('Fully', 'Fully Furnished')], max_length=10, null=True, verbose_name='Interiors')),
                ('kitchen', models.CharField(blank=True, choices=[('Empty', 'Empty'), ('Shelves', 'Shelves'), ('Modular', 'Modular')], max_length=10, null=True, verbose_name='Kitchen')),
                ('plot_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Plot No.')),
                ('cts_no', models.CharField(blank=True, max_length=10, null=True, verbose_name='CTS No.')),
                ('bungalow_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bungalow Name')),
                ('street_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Name')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location')),
                ('landmark', models.CharField(blank=True, max_length=100, null=True, verbose_name='Landmark')),
                ('google_location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Google Location')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('sale_price', models.BigIntegerField(blank=True, null=True, verbose_name='Sale Price')),
                ('ownership', models.CharField(blank=True, choices=[('new', 'New'), ('resale', 'Resale')], max_length=10, null=True, verbose_name='Ownership')),
                ('possession', models.CharField(blank=True, choices=[('ready_to_move', 'Ready To Move'), ('under_construction', 'Under Construction')], max_length=50, null=True, verbose_name='Possession')),
                ('possession_age', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Age of Property')),
                ('possession_due_date', models.DateField(blank=True, null=True, verbose_name='Due Date')),
                ('parking', models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')], null=True, verbose_name='Parking')),
                ('certifications', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('occupation_certificate', 'Occupation Certificate'), ('commencement_certificate', 'Commencement Certificate')], max_length=50, null=True, verbose_name='Available Certifications')),
                ('amenities', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('SWIMMING_POOL', 'Swimming Pool'), ('GYM', 'Gym'), ('GARDEN', 'Garden'), ('ELEVATOR', 'Elevator'), ('VISITOR_PARKING', 'Visitor Parking'), ('WATER_HARVESTING', 'Water Harvesting'), ('SEWAGE_TREATMENT', 'Sewage Treatment'), ('INTERCOM', 'Intercom'), ('STAND_ALONE', 'Stand Alone'), ('GATED_COMPLEX', 'Gated Complex')], max_length=118, null=True, verbose_name='Amenities')),
                ('other_features', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('PIPE_GAS', 'Pipe Gas'), ('PET_FRIENDLY', 'Pet Friendly'), ('BACHELOR_FRIENDLY', 'Bachelor Friendly'), ('FAMILY_ONLY', 'Family Only'), ('WORKING_PROFESSIONALS', 'Working Professionals'), ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'), ('THREE_PHASE_CONNECTION', 'Three Phase Connection'), ('JODI', 'Jodi'), ('EXCLUSIVE_VIEWS', 'Exclusive Views')], max_length=141, null=True, verbose_name='Other Features')),
                ('property_status', models.CharField(blank=True, choices=[('to_confirm', 'To Confirm'), ('active', 'Active'), ('sold', 'Sold')], default='to_confirm', max_length=10, null=True, verbose_name='Property Status')),
                ('delete_flag', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Bungalow',
                'db_table': 'sale_inventory_bungalow',
            },
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='contact_id',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'mr Raj Kumar '), (2, 'Shiva '), (3, 'Rajesh '), (5, 'Mahesh '), (6, 'Salman Bhai '), (10, 'hello '), (4, 'Mallesh '), (11, 'Mars '), (12, 'elon '), (13, 'Jeff '), (7, 'I am ')], max_length=25, null=True, verbose_name='Contact Id'),
        ),
    ]
