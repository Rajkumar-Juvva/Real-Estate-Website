# Generated by Django 4.2 on 2023-04-21 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_label', models.CharField(choices=[('home', 'Home'), ('work', 'Work'), ('other', 'Other')], default='home', max_length=10, verbose_name='Label')),
            ],
            options={
                'db_table': 'phonebook_emails',
            },
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(default='+91', max_length=5)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_label', models.CharField(choices=[('home', 'Home'), ('work', 'Work'), ('other', 'Other')], default='home', max_length=10, verbose_name='Label')),
            ],
            options={
                'db_table': 'phonebook_phones',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prefix')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
                ('suffix', models.CharField(blank=True, max_length=50, null=True, verbose_name='Suffix')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Job Title')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name='Department')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('street_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address')),
                ('street_address_line_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address Line 2')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('pincode', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pincode')),
                ('State', models.CharField(blank=True, max_length=100, null=True, verbose_name='State')),
                ('address_label', models.CharField(choices=[('home', 'Home'), ('work', 'Work'), ('other', 'Other')], default='home', max_length=10, verbose_name='Label')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.BooleanField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by_user', to=settings.AUTH_USER_MODEL)),
                ('email', models.ManyToManyField(to='phonebook.emails')),
                ('phone', models.ManyToManyField(to='phonebook.phones')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'phonebook_contacts',
            },
        ),
    ]
