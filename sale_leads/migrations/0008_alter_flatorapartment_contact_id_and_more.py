# Generated by Django 4.1.8 on 2023-05-09 14:02

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale_leads', '0007_alter_flatorapartment_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatorapartment',
            name='contact_id',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'mr Raj Kumar '), (2, 'Shiva '), (3, 'Rajesh '), (5, 'Mahesh '), (6, 'Salman Bhai '), (10, 'hello '), (4, 'Mallesh '), (11, 'Mars '), (12, 'elon '), (13, 'Jeff '), (7, 'I am ')], max_length=25, null=True, verbose_name='Contact Id'),
        ),
        migrations.AlterField(
            model_name='flatorapartment',
            name='lead_status',
            field=models.CharField(blank=True, choices=[('uncontacted', 'Uncontacted'), ('contacted', 'Contacted'), ('follow_up', 'Follow up'), ('field_visit', 'Field Visit'), ('cold', 'Cold'), ('won', 'Won')], default='uncontacted', max_length=20, null=True, verbose_name='Lead Status'),
        ),
    ]
