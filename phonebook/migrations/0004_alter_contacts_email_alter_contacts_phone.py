# Generated by Django 4.2 on 2023-04-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0003_alter_contacts_created_by_alter_contacts_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.ManyToManyField(blank=True, null=True, to='phonebook.emails'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.ManyToManyField(blank=True, null=True, to='phonebook.phones'),
        ),
    ]
