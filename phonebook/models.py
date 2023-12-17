from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from choices import *
class Emails(models.Model):
    email = models.EmailField(null=True,blank=True)
    email_label = models.CharField(max_length=10, verbose_name='Label',choices=labels, default='home')
    class Meta:
        db_table = "phonebook_emails"
    def __str__(self):
        return self.email+' ('+self.email_label+')'

class Phones(models.Model):
    country_code = models.CharField(max_length=5, default='+91')
    phone = models.CharField(max_length=20,null=True,blank=True)
    phone_label = models.CharField(max_length=10, verbose_name='Label',choices=labels, default='home')
    class Meta:
        db_table = "phonebook_phones"
    def __str__(self):
        return self.country_code+' '+self.phone+' ('+self.phone_label+')'

class Contacts(models.Model):

    # Name
    prefix = models.CharField(max_length=50,verbose_name='Prefix',null=True,blank=True)
    first_name = models.CharField(max_length=100,verbose_name='First Name',null=True,blank=True)
    middle_name = models.CharField(max_length=100,verbose_name='Middle Name',null=True,blank=True)
    last_name = models.CharField(max_length=100,verbose_name='Last Name',null=True,blank=True)
    suffix = models.CharField(max_length=50,verbose_name='Suffix',null=True,blank=True)

    #Details
    company_name = models.CharField(max_length=100,verbose_name='Company Name',null=True,blank=True)
    job_title = models.CharField(max_length=100,verbose_name='Job Title',null=True,blank=True)
    department = models.CharField(max_length=100,verbose_name='Department',null=True,blank=True)
    contact_label = models.CharField(verbose_name="Label", max_length=30, choices=CONTACT_LABELS,null=True,blank=True)


    #contact details
    email = models.ManyToManyField(Emails,null=True,blank=True)
    phone = models.ManyToManyField(Phones,null=True,blank=True)

    #address
    country = models.CharField(max_length=100,verbose_name='Country',null=True,blank=True)
    street_address = models.CharField(max_length=100,verbose_name='Street Address',null=True,blank=True)
    street_address_line_2 = models.CharField(max_length=100,verbose_name='Street Address Line 2',null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name='City',null=True,blank=True)
    pincode = models.CharField(max_length=100,verbose_name='Pincode',null=True,blank=True)
    State = models.CharField(max_length=100,verbose_name='State',null=True,blank=True)
    address_label = models.CharField(max_length=10, verbose_name='Label',choices=labels, default='home')

    birthday = models.DateField(verbose_name='Birthday',null=True,blank=True)
    notes = models.TextField(verbose_name='Notes',null=True,blank=True)

    facebook = models.URLField(blank=True, null=True, verbose_name="Facebook")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    tiktok = models.URLField(blank=True, null=True, verbose_name="TikTok")
    youtube = models.URLField(blank=True, null=True, verbose_name="YouTube")
    custom_link = models.URLField(blank=True, null=True, verbose_name="Custom")

    created_by=models.IntegerField(verbose_name="Created By",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_by=models.IntegerField(verbose_name="Updated By",null=True)
    updated_at = models.DateTimeField(auto_now=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "phonebook_contacts"
        verbose_name = "Contacts"
    
    def __str__(self):
        return self.give_full_name()
    
    
    def give_full_name(self):
        return (self.prefix+' ' if self.prefix else '')+(self.first_name+' ' if self.first_name else '')+(self.middle_name+' ' if self.middle_name else '')+(self.last_name+' ' if self.last_name else '')+(self.suffix if self.suffix else '')
