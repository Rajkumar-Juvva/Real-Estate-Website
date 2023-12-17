# Generated by Django 4.2 on 2023-04-23 18:10

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatorapartment',
            name='certifications',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('occupation_certificate', 'Occupation Certificate'), ('commencement_certificate', 'Commencement Certificate')], max_length=50, null=True, verbose_name='Available Certifications'),
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='contact_id',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[], max_length=200, null=True, verbose_name='Contact Id'),
        ),
    ]