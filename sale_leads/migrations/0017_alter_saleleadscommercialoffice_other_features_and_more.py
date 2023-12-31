# Generated by Django 4.1.7 on 2023-06-06 12:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_leads', '0016_saleleadscottage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleleadscommercialoffice',
            name='other_features',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MEZANINE', 'Mezanine'), ('ROAD_FACING', 'Road Facing'), ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'), ('THREE_PHASE_CONNECTION', 'Three Phase Connection'), ('FIRE_EXIT', 'Fire Exit'), ('PILLARLESS', 'Pillarless'), ('JODI', 'Jodi')], max_length=93, null=True, verbose_name='Other Features'),
        ),
        migrations.AlterField(
            model_name='saleleadscommercialoffice',
            name='pantry',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], max_length=10, null=True, verbose_name='Pantry'),
        ),
        migrations.AlterField(
            model_name='saleleadscottage',
            name='other_features',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ROAD_TOUCH', 'Road Touch'), ('JODI', 'Jodi'), ('MEZANINE', 'Mezanine'), ('BASEMENT', 'Basement'), ('ROAD_FACING', 'Road Facing'), ('WATER_CONNECTION', 'Water Connection'), ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'), ('THREE_PHASE_CONNECTION', 'Three Phase Connection'), ('FIRE_EXIT', 'Fire Exit'), ('PILLARLESS', 'Pillarless'), ('GAS_PIPELINE', 'Gas Pipeline')], max_length=143, null=True, verbose_name='Other Features'),
        ),
        migrations.AlterField(
            model_name='saleleadsshop',
            name='other_features',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ROAD_TOUCH', 'Road Touch'), ('JODI', 'Jodi'), ('MEZANINE', 'Mezanine'), ('BASEMENT', 'Basement'), ('ROAD_FACING', 'Road Facing'), ('WATER_CONNECTION', 'Water Connection'), ('SINGLE_PHASE_CONNECTION', 'Single Phase Connection'), ('THREE_PHASE_CONNECTION', 'Three Phase Connection'), ('FIRE_EXIT', 'Fire Exit'), ('PILLARLESS', 'Pillarless'), ('GAS_PIPELINE', 'Gas Pipeline')], max_length=143, null=True, verbose_name='Other Features'),
        ),
    ]
