from django.db import models
from django.contrib.auth.models import User
from phonebook.models import Contacts
from choices import *
from multiselectfield import MultiSelectField
from django import forms



# Create your models here.

class flatOrApartment(models.Model):
    CHOICES = ((obj.id,obj.give_full_name()) for obj in Contacts.objects.all())
    contact_id = MultiSelectField(verbose_name="Contact Id",choices=CHOICES,null=True,blank=True)
    property_utility = MultiSelectField(verbose_name="Property Utility",choices=PROPERTY_UTILITY_CHOICES,null=True,blank=True)
    tags =  models.TextField(verbose_name="Tags",null=True,blank=True)
    notes =  models.TextField(verbose_name="Notes",null=True,blank=True)
    inventory_id = models.BigIntegerField(verbose_name="Inventory Id",unique=True)

    created_by=models.IntegerField(verbose_name="Created By",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_by=models.IntegerField(verbose_name="Updated By",null=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_link = models.CharField(max_length=100,verbose_name="Video Link",null=True,blank=True)
    description = models.TextField(verbose_name="Description",null=True,blank=True)

    #<----   ----->#
    bedroom = models.CharField(verbose_name="Bedroom", max_length=5, choices=BEDROOM_CHOICES,null=True,blank=True)
    bathroom = models.IntegerField(verbose_name="Bathroom", choices=BATHROOM_CHOICES,null=True,blank=True)
    carpet_units = models.CharField(verbose_name="Carpet Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    carpet_area_min = models.IntegerField(verbose_name="Carpet Area Min",null=True,blank=True)
    carpet_area_max = models.IntegerField(verbose_name="Carpet Area Max",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area_min = models.IntegerField(verbose_name="Built-up Area Min",null=True,blank=True)
    builtup_area_max = models.IntegerField(verbose_name="Built-up Area Max",null=True,blank=True)
    floor_min = models.IntegerField(verbose_name="Floor Min", choices=FLOOR_CHOICES,null=True,blank=True)
    floor_max = models.IntegerField(verbose_name="Floor Max", choices=FLOOR_CHOICES,null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = MultiSelectField(verbose_name="Vastu / Exit", max_length=5, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = MultiSelectField(verbose_name="Interiors", max_length=10, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = MultiSelectField(verbose_name="Kitchen", max_length=10, choices=KITCHEN_CHOICES,null=True,blank=True)  
    
    #<----   ----->#
    location = MultiSelectField(verbose_name="Location",choices=(),null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    budget_min = models.BigIntegerField(verbose_name='Minimum Budget',null=True,blank=True)
    budget_max = models.BigIntegerField(verbose_name='Maximum Budget',null=True,blank=True)
    ownership = MultiSelectField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = MultiSelectField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=60, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES,null=True,blank=True)
    lead_status = models.CharField(verbose_name='Lead Status', max_length=20, choices=LEAD_STATUS_CHOICES, default='uncontacted',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_lead_flat_or_apartment"
        verbose_name = "Flat or Apartment"
    
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = flatOrApartment.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 50000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
    def __str__(self):
        return str(self.inventory_id)
    
class SaleLeadsBungalow(models.Model):
    CHOICES = ((obj.id,obj.give_full_name()) for obj in Contacts.objects.all())
    contact_id = MultiSelectField(verbose_name="Contact Id",choices=CHOICES,null=True,blank=True)
    property_utility = MultiSelectField(verbose_name="Property Utility",choices=PROPERTY_UTILITY_CHOICES,null=True,blank=True)
    tags =  models.TextField(verbose_name="Tags",null=True,blank=True)
    notes =  models.TextField(verbose_name="Notes",null=True,blank=True)
    inventory_id = models.BigIntegerField(verbose_name="Inventory Id",unique=True)

    created_by=models.IntegerField(verbose_name="Created By",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_by=models.IntegerField(verbose_name="Updated By",null=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_link = models.CharField(max_length=100,verbose_name="Video Link",null=True,blank=True)
    description = models.TextField(verbose_name="Description",null=True,blank=True)

    #<----   ----->#
    bedroom = models.CharField(verbose_name="Bedroom", max_length=5, choices=BEDROOM_CHOICES,null=True,blank=True)
    bathroom = models.IntegerField(verbose_name="Bathroom", choices=BATHROOM_CHOICES,null=True,blank=True)
    carpet_units = models.CharField(verbose_name="Carpet Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    carpet_area_min = models.IntegerField(verbose_name="Carpet Area Min",null=True,blank=True)
    carpet_area_max = models.IntegerField(verbose_name="Carpet Area Max",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area_min = models.IntegerField(verbose_name="Built-up Area Min",null=True,blank=True)
    builtup_area_max = models.IntegerField(verbose_name="Built-up Area Max",null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    open_space = MultiSelectField(verbose_name="Open Space",choices=OPEN_SPACE_CHOICES,null=True,blank=True)
    vastu_exit = MultiSelectField(verbose_name="Vastu / Exit", max_length=30, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = MultiSelectField(verbose_name="Interiors", max_length=30, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = MultiSelectField(verbose_name="Kitchen", max_length=30, choices=KITCHEN_CHOICES,null=True,blank=True)  
    
    #<----   ----->#
    location = MultiSelectField(verbose_name="Location",choices=(),null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    budget_min = models.BigIntegerField(verbose_name='Minimum Budget',null=True,blank=True)
    budget_max = models.BigIntegerField(verbose_name='Maximum Budget',null=True,blank=True)
    ownership = MultiSelectField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = MultiSelectField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=60, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES,null=True,blank=True)
    lead_status = models.CharField(verbose_name='Lead Status', max_length=20, choices=LEAD_STATUS_CHOICES, default='uncontacted',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_lead_bungalow"
        verbose_name = "Bungalow"
    
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleLeadsBungalow.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 51000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
    def __str__(self):
        return str(self.inventory_id)
    

class SaleLeadsPenthouse(models.Model):
    CHOICES = ((obj.id,obj.give_full_name()) for obj in Contacts.objects.all())
    contact_id = MultiSelectField(verbose_name="Contact Id",choices=CHOICES,null=True,blank=True)
    property_utility = MultiSelectField(verbose_name="Property Utility",choices=PROPERTY_UTILITY_CHOICES,null=True,blank=True)
    tags =  models.TextField(verbose_name="Tags",null=True,blank=True)
    notes =  models.TextField(verbose_name="Notes",null=True,blank=True)
    inventory_id = models.BigIntegerField(verbose_name="Inventory Id",unique=True)

    created_by=models.IntegerField(verbose_name="Created By",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_by=models.IntegerField(verbose_name="Updated By",null=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_link = models.CharField(max_length=100,verbose_name="Video Link",null=True,blank=True)
    description = models.TextField(verbose_name="Description",null=True,blank=True)

    #<----   ----->#
    bedroom = models.CharField(verbose_name="Bedroom", max_length=5, choices=BEDROOM_CHOICES,null=True,blank=True)
    bathroom = models.IntegerField(verbose_name="Bathroom", choices=BATHROOM_CHOICES,null=True,blank=True)
    carpet_units = models.CharField(verbose_name="Carpet Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    carpet_area_min = models.IntegerField(verbose_name="Carpet Area Min",null=True,blank=True)
    carpet_area_max = models.IntegerField(verbose_name="Carpet Area Max",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area_min = models.IntegerField(verbose_name="Built-up Area Min",null=True,blank=True)
    builtup_area_max = models.IntegerField(verbose_name="Built-up Area Max",null=True,blank=True)
    floor_min = models.IntegerField(verbose_name="Floor Min", choices=FLOOR_CHOICES,null=True,blank=True)
    floor_max = models.IntegerField(verbose_name="Floor Max", choices=FLOOR_CHOICES,null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = MultiSelectField(verbose_name="Vastu / Exit", max_length=5, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = MultiSelectField(verbose_name="Interiors", max_length=10, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = MultiSelectField(verbose_name="Kitchen", max_length=10, choices=KITCHEN_CHOICES,null=True,blank=True)  
    
    #<----   ----->#
    location = MultiSelectField(verbose_name="Location",choices=(),null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    budget_min = models.BigIntegerField(verbose_name='Minimum Budget',null=True,blank=True)
    budget_max = models.BigIntegerField(verbose_name='Maximum Budget',null=True,blank=True)
    ownership = MultiSelectField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = MultiSelectField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=60, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES,null=True,blank=True)
    lead_status = models.CharField(verbose_name='Lead Status', max_length=20, choices=LEAD_STATUS_CHOICES, default='uncontacted',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_lead_penthouse"
        verbose_name = "Penthouse"
    
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleLeadsPenthouse.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 52000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
    def __str__(self):
        return str(self.inventory_id)
    
class SaleLeadsCommercialOffice(models.Model):
    CHOICES = ((obj.id,obj.give_full_name()) for obj in Contacts.objects.all())
    contact_id = MultiSelectField(verbose_name="Contact Id",choices=CHOICES,null=True,blank=True)
    property_utility = MultiSelectField(verbose_name="Property Utility",choices=PROPERTY_UTILITY_CHOICES,null=True,blank=True)
    tags =  models.TextField(verbose_name="Tags",null=True,blank=True)
    notes =  models.TextField(verbose_name="Notes",null=True,blank=True)
    inventory_id = models.BigIntegerField(verbose_name="Inventory Id",unique=True)

    created_by=models.IntegerField(verbose_name="Created By",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_by=models.IntegerField(verbose_name="Updated By",null=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_link = models.CharField(max_length=100,verbose_name="Video Link",null=True,blank=True)
    description = models.TextField(verbose_name="Description",null=True,blank=True)

    #<----   ----->#
    cabin = models.IntegerField(verbose_name="Cabin", null=True,blank=True)
    work_stations = models.IntegerField(verbose_name="Work Stations",null=True,blank=True)
    bathroom = models.IntegerField(verbose_name="Bathroom", choices=BATHROOM_CHOICES,null=True,blank=True)
    carpet_units = models.CharField(verbose_name="Carpet Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    carpet_area_min = models.IntegerField(verbose_name="Carpet Area Min",null=True,blank=True)
    carpet_area_max = models.IntegerField(verbose_name="Carpet Area Max",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area_min = models.IntegerField(verbose_name="Built-up Area Min",null=True,blank=True)
    builtup_area_max = models.IntegerField(verbose_name="Built-up Area Max",null=True,blank=True)
    floor_min = models.IntegerField(verbose_name="Floor Min", choices=FLOOR_CHOICES,null=True,blank=True)
    floor_max = models.IntegerField(verbose_name="Floor Max", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = MultiSelectField(verbose_name="Vastu / Exit", max_length=5, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = MultiSelectField(verbose_name="Interiors", max_length=10, choices=INTERIORS_CHOICES,null=True,blank=True)
    pantry = MultiSelectField(verbose_name="Pantry", max_length=10, choices=PANTRY_CHOICES,null=True,blank=True)  
    
    #<----   ----->#
    location = MultiSelectField(verbose_name="Location",choices=(),null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    budget_min = models.BigIntegerField(verbose_name='Minimum Budget',null=True,blank=True)
    budget_max = models.BigIntegerField(verbose_name='Maximum Budget',null=True,blank=True)
    ownership = MultiSelectField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = MultiSelectField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=60, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES_COMMERCIAL_OFFICE,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES_COMMERCIAL_OFFICE,null=True,blank=True)
    lead_status = models.CharField(verbose_name='Lead Status', max_length=20, choices=LEAD_STATUS_CHOICES, default='uncontacted',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_lead_commercial_office"
        verbose_name = "Commercial Office"
    
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleLeadsCommercialOffice.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 53000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
    def __str__(self):
        return str(self.inventory_id)

class SaleLeadsShop(models.Model):
    CHOICES = ((obj.id,obj.give_full_name()) for obj in Contacts.objects.all())
    contact_id = MultiSelectField(verbose_name="Contact Id",choices=CHOICES,null=True,blank=True)
    property_utility = MultiSelectField(verbose_name="Property Utility",choices=PROPERTY_UTILITY_CHOICES,null=True,blank=True)
    tags =  models.TextField(verbose_name="Tags",null=True,blank=True)
    notes =  models.TextField(verbose_name="Notes",null=True,blank=True)
    inventory_id = models.BigIntegerField(verbose_name="Inventory Id",unique=True)

    created_by=models.IntegerField(verbose_name="Created By",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_by=models.IntegerField(verbose_name="Updated By",null=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_link = models.CharField(max_length=100,verbose_name="Video Link",null=True,blank=True)
    description = models.TextField(verbose_name="Description",null=True,blank=True)

    #<----   ----->#
    partitions = models.IntegerField(verbose_name="Partitions", null=True,blank=True)
    bathroom = models.IntegerField(verbose_name="Bathroom", choices=BATHROOM_CHOICES,null=True,blank=True)
    carpet_units = models.CharField(verbose_name="Carpet Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    carpet_area_min = models.IntegerField(verbose_name="Carpet Area Min",null=True,blank=True)
    carpet_area_max = models.IntegerField(verbose_name="Carpet Area Max",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area_min = models.IntegerField(verbose_name="Built-up Area Min",null=True,blank=True)
    builtup_area_max = models.IntegerField(verbose_name="Built-up Area Max",null=True,blank=True)
    floor_min = models.IntegerField(verbose_name="Floor Min", choices=FLOOR_CHOICES,null=True,blank=True)
    floor_max = models.IntegerField(verbose_name="Floor Max", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = MultiSelectField(verbose_name="Vastu / Exit", max_length=5, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = MultiSelectField(verbose_name="Interiors", max_length=10, choices=INTERIORS_CHOICES,null=True,blank=True)
    
    #<----   ----->#
    location = MultiSelectField(verbose_name="Location",choices=(),null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    budget_min = models.BigIntegerField(verbose_name='Minimum Budget',null=True,blank=True)
    budget_max = models.BigIntegerField(verbose_name='Maximum Budget',null=True,blank=True)
    ownership = MultiSelectField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = MultiSelectField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=60, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES_SHOP,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES_SHOP,null=True,blank=True)
    lead_status = models.CharField(verbose_name='Lead Status', max_length=20, choices=LEAD_STATUS_CHOICES, default='uncontacted',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_lead_shop"
        verbose_name = "Shop"
    
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleLeadsShop.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 54000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
    def __str__(self):
        return str(self.inventory_id)
    
class SaleLeadsCottage(models.Model):
    CHOICES = ((obj.id,obj.give_full_name()) for obj in Contacts.objects.all())
    contact_id = MultiSelectField(verbose_name="Contact Id",choices=CHOICES,null=True,blank=True)
    property_utility = MultiSelectField(verbose_name="Property Utility",choices=PROPERTY_UTILITY_CHOICES,null=True,blank=True)
    tags =  models.TextField(verbose_name="Tags",null=True,blank=True)
    notes =  models.TextField(verbose_name="Notes",null=True,blank=True)
    inventory_id = models.BigIntegerField(verbose_name="Inventory Id",unique=True)

    created_by=models.IntegerField(verbose_name="Created By",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_by=models.IntegerField(verbose_name="Updated By",null=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_link = models.CharField(max_length=100,verbose_name="Video Link",null=True,blank=True)
    description = models.TextField(verbose_name="Description",null=True,blank=True)

    #<----   ----->#
    partitions = models.IntegerField(verbose_name="Partitions", null=True,blank=True)
    bathroom = models.IntegerField(verbose_name="Bathroom", choices=BATHROOM_CHOICES,null=True,blank=True)
    carpet_units = models.CharField(verbose_name="Carpet Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    carpet_area_min = models.IntegerField(verbose_name="Carpet Area Min",null=True,blank=True)
    carpet_area_max = models.IntegerField(verbose_name="Carpet Area Max",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area_min = models.IntegerField(verbose_name="Built-up Area Min",null=True,blank=True)
    builtup_area_max = models.IntegerField(verbose_name="Built-up Area Max",null=True,blank=True)
    floor_min = models.IntegerField(verbose_name="Floor Min", choices=FLOOR_CHOICES,null=True,blank=True)
    floor_max = models.IntegerField(verbose_name="Floor Max", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = MultiSelectField(verbose_name="Vastu / Exit", max_length=5, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = MultiSelectField(verbose_name="Interiors", max_length=30, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = MultiSelectField(verbose_name="Kitchen", max_length=30, choices=KITCHEN_CHOICES,null=True,blank=True)
    
    #<----   ----->#
    location = MultiSelectField(verbose_name="Location",choices=(),null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    budget_min = models.BigIntegerField(verbose_name='Minimum Budget',null=True,blank=True)
    budget_max = models.BigIntegerField(verbose_name='Maximum Budget',null=True,blank=True)
    ownership = MultiSelectField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = MultiSelectField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=60, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICE_COTTAGE,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES_COTTAGE,null=True,blank=True)
    lead_status = models.CharField(verbose_name='Lead Status', max_length=20, choices=LEAD_STATUS_CHOICES, default='uncontacted',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_lead_cottage"
        verbose_name = "Cottage"
    
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleLeadsCottage.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 55000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
    def __str__(self):
        return str(self.inventory_id)