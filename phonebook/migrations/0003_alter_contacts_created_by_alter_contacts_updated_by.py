# Generated by Django 4.2 on 2023-04-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_alter_contacts_options_alter_contacts_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='created_by',
            field=models.IntegerField(null=True, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='updated_by',
            field=models.IntegerField(null=True, verbose_name='Updated By'),
        ),
    ]
