# Generated by Django 4.1.8 on 2023-04-24 17:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_inventory', '0002_alter_flatorapartment_certifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatorapartment',
            name='contact_id',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'mr Raj Kumar '), (2, 'Shiva '), (3, 'Rajesh '), (4, 'Mallesh '), (5, 'Mahesh '), (6, 'Salman Bhai '), (8, ''), (9, ''), (7, 'I am '), (10, 'hello ')], max_length=20, null=True, verbose_name='Contact Id'),
        ),
    ]
