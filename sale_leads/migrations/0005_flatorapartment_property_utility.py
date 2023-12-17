# Generated by Django 4.1.8 on 2023-04-26 14:09

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_leads', '0004_alter_flatorapartment_contact_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatorapartment',
            name='property_utility',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Industrial', 'Industrial'), ('Agricultural', 'Agricultural'), ('Restaurant / Dinner', 'Restaurant / Dinner'), ('Lodging / Hotel', 'Lodging / Hotel'), ('Educational', 'Educational'), ('Recreational', 'Recreational'), ('Hospital', 'Hospital')], max_length=116, null=True, verbose_name='Property Utility'),
        ),
    ]
