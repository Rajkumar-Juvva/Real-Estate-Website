# Generated by Django 4.1.8 on 2023-05-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0005_contacts_contact_label_contacts_custom_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='custom_link',
            field=models.URLField(blank=True, null=True, verbose_name='Custom'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='LinkedIn'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='tiktok',
            field=models.URLField(blank=True, null=True, verbose_name='TikTok'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='YouTube'),
        ),
    ]
