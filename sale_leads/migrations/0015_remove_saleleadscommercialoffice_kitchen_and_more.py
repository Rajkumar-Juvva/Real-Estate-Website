# Generated by Django 4.1.7 on 2023-05-31 14:28

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_leads', '0014_saleleadscommercialoffice_saleleadsshop_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleleadscommercialoffice',
            name='kitchen',
        ),
        migrations.AddField(
            model_name='saleleadscommercialoffice',
            name='pantry',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Empty', 'Empty'), ('Shelves', 'Shelves'), ('Modular', 'Modular')], max_length=10, null=True, verbose_name='Pantry'),
        ),
    ]
