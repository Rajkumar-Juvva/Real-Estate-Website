from django.db import models
from django.contrib.auth.models import User
from phonebook.models import Contacts
from choices import *
from multiselectfield import MultiSelectField

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
    carpet_area = models.IntegerField(verbose_name="Carpet Area",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area = models.IntegerField(verbose_name="Built-up Area",null=True,blank=True)
    floor = models.IntegerField(verbose_name="Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = models.CharField(verbose_name="Vastu / Exit", max_length=30, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = models.CharField(verbose_name="Interiors", max_length=30, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = models.CharField(verbose_name="Kitchen", max_length=30, choices=KITCHEN_CHOICES,null=True,blank=True)  
    
    #<----   ----->#
    flat_number = models.CharField(verbose_name="Flat No.",max_length=10,null=True,blank=True)
    wing = models.CharField(verbose_name="Wing", max_length=9,null=True,blank=True)
    building_name = models.CharField(max_length=100,verbose_name="Building Name",null=True,blank=True)
    street_name = models.CharField(max_length=100,verbose_name="Street Name",null=True,blank=True)
    location = models.CharField(max_length=100,verbose_name="Location",null=True,blank=True)
    landmark = models.CharField(max_length=100,verbose_name="Landmark",null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    sale_price = models.BigIntegerField(verbose_name='Sale Price',null=True,blank=True)
    ownership = models.CharField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = models.CharField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=50, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES,null=True,blank=True)
    property_status = models.CharField(verbose_name='Property Status', max_length=10, choices=PROPERTY_STATUS_CHOICES, default='to_confirm',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_inventory_flat_or_apartment"
        verbose_name = "Flat or Apartment"
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = flatOrApartment.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 60000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.inventory_id)
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    

class SaleInventoryBungalow(models.Model):
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
    carpet_area = models.IntegerField(verbose_name="Carpet Area",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area = models.IntegerField(verbose_name="Built-up Area",null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    open_space = MultiSelectField(verbose_name="Open Space",choices=OPEN_SPACE_CHOICES,null=True,blank=True)
    vastu_exit = models.CharField(verbose_name="Vastu / Exit", max_length=5, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = models.CharField(verbose_name="Interiors", max_length=10, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = models.CharField(verbose_name="Kitchen", max_length=10, choices=KITCHEN_CHOICES,null=True,blank=True)  
    
    #<----   ----->#
    plot_number = models.CharField(verbose_name="Plot No.",max_length=10,null=True,blank=True)
    cts_no = models.CharField(verbose_name="CTS No.",max_length=10,null=True,blank=True)
    bungalow_name = models.CharField(max_length=100,verbose_name="Bungalow Name",null=True,blank=True)
    street_name = models.CharField(max_length=100,verbose_name="Street Name",null=True,blank=True)
    location = models.CharField(max_length=100,verbose_name="Location",null=True,blank=True)
    landmark = models.CharField(max_length=100,verbose_name="Landmark",null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    sale_price = models.BigIntegerField(verbose_name='Sale Price',null=True,blank=True)
    ownership = models.CharField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = models.CharField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=50, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES,null=True,blank=True)
    property_status = models.CharField(verbose_name='Property Status', max_length=10, choices=PROPERTY_STATUS_CHOICES, default='to_confirm',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_inventory_bungalow"
        verbose_name = "Bungalow"
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleInventoryBungalow.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 6100000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.inventory_id)
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
class SaleInventoryPenthouse(models.Model):
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
    carpet_area = models.IntegerField(verbose_name="Carpet Area",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area = models.IntegerField(verbose_name="Built-up Area",null=True,blank=True)
    floor = models.IntegerField(verbose_name="Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = models.CharField(verbose_name="Vastu / Exit", max_length=30, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = models.CharField(verbose_name="Interiors", max_length=30, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = models.CharField(verbose_name="Kitchen", max_length=30, choices=KITCHEN_CHOICES,null=True,blank=True)  
    
    #<----   ----->#
    flat_number = models.CharField(verbose_name="Flat No.",max_length=10,null=True,blank=True)
    wing = models.CharField(verbose_name="Wing", max_length=9,null=True,blank=True)
    building_name = models.CharField(max_length=100,verbose_name="Building Name",null=True,blank=True)
    street_name = models.CharField(max_length=100,verbose_name="Street Name",null=True,blank=True)
    location = models.CharField(max_length=100,verbose_name="Location",null=True,blank=True)
    landmark = models.CharField(max_length=100,verbose_name="Landmark",null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    sale_price = models.BigIntegerField(verbose_name='Sale Price',null=True,blank=True)
    ownership = models.CharField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = models.CharField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=50, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES,null=True,blank=True)
    property_status = models.CharField(verbose_name='Property Status', max_length=10, choices=PROPERTY_STATUS_CHOICES, default='to_confirm',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_inventory_Penthouse"
        verbose_name = "Penthouse"
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleInventoryPenthouse.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 62000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.inventory_id)
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
class SaleInventoryCommercialOffice(models.Model):
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
    carpet_area = models.IntegerField(verbose_name="Carpet Area",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area = models.IntegerField(verbose_name="Built-up Area",null=True,blank=True)
    floor = models.IntegerField(verbose_name="Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = models.CharField(verbose_name="Vastu / Exit", max_length=30, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = models.CharField(verbose_name="Interiors", max_length=30, choices=INTERIORS_CHOICES,null=True,blank=True)
    pantry = models.IntegerField(verbose_name="Pantry", null=True,blank=True)  
    
    #<----   ----->#
    office_no = models.CharField(verbose_name="Office No.",max_length=10,null=True,blank=True)
    wing = models.CharField(verbose_name="Wing", max_length=9,null=True,blank=True)
    building_name = models.CharField(max_length=100,verbose_name="Building Name",null=True,blank=True)
    street_name = models.CharField(max_length=100,verbose_name="Street Name",null=True,blank=True)
    location = models.CharField(max_length=100,verbose_name="Location",null=True,blank=True)
    landmark = models.CharField(max_length=100,verbose_name="Landmark",null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    sale_price = models.BigIntegerField(verbose_name='Sale Price',null=True,blank=True)
    ownership = models.CharField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = models.CharField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=50, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES_COMMERCIAL_OFFICE,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES_COMMERCIAL_OFFICE,null=True,blank=True)
    property_status = models.CharField(verbose_name='Property Status', max_length=10, choices=PROPERTY_STATUS_CHOICES, default='to_confirm',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_inventory_commercial_office"
        verbose_name = "Commercial Office"
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleInventoryCommercialOffice.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 63000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.inventory_id)
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
class SaleInventoryShop(models.Model):
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
    carpet_area = models.IntegerField(verbose_name="Carpet Area",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area = models.IntegerField(verbose_name="Built-up Area",null=True,blank=True)
    floor = models.IntegerField(verbose_name="Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floor", choices=FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = models.CharField(verbose_name="Vastu / Exit", max_length=30, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = models.CharField(verbose_name="Interiors", max_length=30, choices=INTERIORS_CHOICES,null=True,blank=True)
    
    #<----   ----->#
    shop_no = models.CharField(verbose_name="Shop No.",max_length=30,null=True,blank=True)
    wing = models.CharField(verbose_name="Wing", max_length=30,null=True,blank=True)
    building_name = models.CharField(max_length=100,verbose_name="Building Name",null=True,blank=True)
    street_name = models.CharField(max_length=100,verbose_name="Street Name",null=True,blank=True)
    location = models.CharField(max_length=100,verbose_name="Location",null=True,blank=True)
    landmark = models.CharField(max_length=100,verbose_name="Landmark",null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    sale_price = models.BigIntegerField(verbose_name='Sale Price',null=True,blank=True)
    ownership = models.CharField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = models.CharField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=50, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICES_SHOP,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES_SHOP,null=True,blank=True)
    property_status = models.CharField(verbose_name='Property Status', max_length=10, choices=PROPERTY_STATUS_CHOICES, default='to_confirm',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_inventory_shop"
        verbose_name = "Shop"
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleInventoryShop.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 64000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.inventory_id)
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)
    
class SaleInventoryCottage(models.Model):
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
    carpet_area = models.IntegerField(verbose_name="Carpet Area",null=True,blank=True)
    builtup_units = models.CharField(verbose_name="Built-up Units", max_length=5, choices=AREA_UNITS_CHOICES,null=True,blank=True)
    builtup_area = models.IntegerField(verbose_name="Built-up Area",null=True,blank=True)
    total_floor = models.IntegerField(verbose_name="Total Floors", choices=TOTAL_FLOOR_CHOICES,null=True,blank=True)
    vastu_exit = models.CharField(verbose_name="Vastu / Exit", max_length=30, choices=VASTU_EXIT_CHOICES,null=True,blank=True)
    interiors = models.CharField(verbose_name="Interiors", max_length=30, choices=INTERIORS_CHOICES,null=True,blank=True)
    kitchen = models.CharField(verbose_name="Kitchen", max_length=30, choices=KITCHEN_CHOICES,null=True,blank=True)
    
    #<----   ----->#
    room_no = models.CharField(verbose_name="Room No.",max_length=30,null=True,blank=True)
    cts_no = models.CharField(verbose_name="CTS No", max_length=30,null=True,blank=True)
    society_name = models.CharField(max_length=100,verbose_name="Society Name",null=True,blank=True)
    street_name = models.CharField(max_length=100,verbose_name="Street Name",null=True,blank=True)
    location = models.CharField(max_length=100,verbose_name="Location",null=True,blank=True)
    landmark = models.CharField(max_length=100,verbose_name="Landmark",null=True,blank=True)
    google_location = models.CharField(max_length=200,verbose_name="Google Location",null=True,blank=True)
    city = models.CharField(max_length=100,verbose_name="City",null=True,blank=True)
    state = models.CharField(max_length=100,verbose_name="State",null=True,blank=True)
    country = models.CharField(max_length=100,verbose_name="Country",null=True,blank=True)
    
    #<----   ----->#
    sale_price = models.BigIntegerField(verbose_name='Sale Price',null=True,blank=True)
    ownership = models.CharField(verbose_name='Ownership', max_length=10, choices=SALE_CHOICES,null=True,blank=True)
    possession = models.CharField(verbose_name='Possession', max_length=50, choices = POSSESSION_CHOICES,null=True,blank=True)
    possession_age = models.PositiveSmallIntegerField(verbose_name='Age of Property', blank=True, null=True,)
    possession_due_date = models.DateField(verbose_name='Due Date', null=True,blank=True)
    parking = models.IntegerField(verbose_name='Parking', choices=PARKING_CHOICES,null=True,blank=True)
    certifications = MultiSelectField(verbose_name='Available Certifications', max_length=50, choices=CERTIFICATION_CHOICES,null=True,blank=True)

    #<----   ----->#
    amenities = MultiSelectField(verbose_name='Amenities', choices = AMENITIES_CHOICE_COTTAGE,null=True,blank=True)
    other_features = MultiSelectField(verbose_name='Other Features', choices = OTHER_FEATURES_CHOICES_COTTAGE,null=True,blank=True)
    property_status = models.CharField(verbose_name='Property Status', max_length=10, choices=PROPERTY_STATUS_CHOICES, default='to_confirm',null=True,blank=True)

    delete_flag = models.BooleanField(null=True,blank=True)

    class Meta:
        db_table = "sale_inventory_cottage"
        verbose_name = "Cottage"
    def save(self,*args,**kwargs):
        if not self.inventory_id:
            latest = SaleInventoryCottage.objects.order_by('-id').first()
            if latest:
                inventory_id = int(latest.inventory_id) + 1
            else:
                inventory_id = 65000000000000
            self.inventory_id = str(inventory_id).zfill(15)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.inventory_id)
    def selected_contacts(self):
        '''
            This method will return selected contacts to show in admin dashboard
        '''
        return str(self.contact_id)