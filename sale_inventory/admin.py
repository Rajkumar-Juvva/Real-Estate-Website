from django.contrib import admin
from .models import *
from .forms import *
from django import forms
from choices import *

class PropertyUtilityFilter(admin.SimpleListFilter):
    title = 'Property Utility'
    parameter_name = 'property_utility'

    def lookups(self, request, model_admin):
        return PROPERTY_UTILITY_CHOICES

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            # Filter the queryset to include only instances that have at least one matching value in the property_utility field
            return queryset.filter(property_utility__icontains=value)
        return queryset
    
class SaleInventoryFlatOrApartmentAdminClass(admin.ModelAdmin):
    form = SaleInventoryFlatOrApartmentForm
    actions = ['mark_as_delete_flag']
    list_filter = ('property_status', PropertyUtilityFilter,'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','bedroom','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','bedroom','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    
    fieldsets = (
    ('Contact Info', {
        'fields': ('contact_id', 'tags', 'notes'),
        'classes': ('',)
    }),
    ('Property Info', {
        'fields': ('property_utility',('bedroom', 'bathroom'), ('carpet_units', 'carpet_area'), ('builtup_units', 'builtup_area'), ('floor', 'total_floor'), 'vastu_exit', 'interiors', 'kitchen'),
        "classes": ('',)
    }),
    ('Location Info', {
        'fields': ('flat_number', 'wing', 'building_name', 'street_name','location', 'landmark', 'google_location', 'city', 'state', 'country'),
        'classes': ('',)
    }),
    ('Budget Info', {
        'fields': (('sale_price', 'ownership'), 'possession', 'possession_age', 'possession_due_date', 'parking', 'certifications'),
        'classes': ('',)
    }),
    ('Features Info', {
        'fields': ('amenities', 'other_features'),
        'classes': ('',)
    }),
    ('Inventory Info', {
        'fields': ( 'video_link', 'description'),
        'classes': ('',)
    }),
    ('Status Info', {
        'fields': ('property_status', 'delete_flag'),
        'classes': ('',)
    })
    )


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        obj.save()

    class Media:
        js = ('sale_inventory/js/possession_field.js',)

admin.site.register(flatOrApartment, SaleInventoryFlatOrApartmentAdminClass)

#Bungalow

class SaleInventoryBungalowAdminClass(admin.ModelAdmin):
    form = SaleInventoryBungalowForm
    actions = ['mark_as_delete_flag']
    list_filter = ('property_status', PropertyUtilityFilter,'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','bedroom','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','total_floor','open_space','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','bedroom','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','total_floor','open_space','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    
    fieldsets = (
    ('Contact Info', {
        'fields': ('contact_id', 'tags', 'notes'),
        'classes': ('',)
    }),
    ('Property Info', {
        'fields': ('property_utility',('bedroom', 'bathroom'), ('carpet_units', 'carpet_area'), ('builtup_units', 'builtup_area'), 'total_floor','open_space', 'vastu_exit', 'interiors', 'kitchen'),
        "classes": ('',)
    }),
    ('Location Info', {
        'fields': ('plot_number','bungalow_name', 'street_name','location', 'landmark', 'google_location', 'city', 'state', 'country'),
        'classes': ('',)
    }),
    ('Budget Info', {
        'fields': (('sale_price', 'ownership'), 'possession', 'possession_age', 'possession_due_date', 'parking', 'certifications'),
        'classes': ('',)
    }),
    ('Features Info', {
        'fields': ('amenities', 'other_features'),
        'classes': ('',)
    }),
    ('Inventory Info', {
        'fields': ( 'video_link', 'description'),
        'classes': ('',)
    }),
    ('Status Info', {
        'fields': ('property_status', 'delete_flag'),
        'classes': ('',)
    })
    )


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        obj.save()

    class Media:
        js = ('sale_inventory/js/possession_field.js',)

admin.site.register(SaleInventoryBungalow, SaleInventoryBungalowAdminClass)


#Penthouse
class SaleInventoryPenthouseAdminClass(admin.ModelAdmin):
    form = SaleInventoryPenthouseForm
    actions = ['mark_as_delete_flag']
    list_filter = ('property_status', PropertyUtilityFilter,'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','bedroom','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','bedroom','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    
    fieldsets = (
    ('Contact Info', {
        'fields': ('contact_id', 'tags', 'notes'),
        'classes': ('',)
    }),
    ('Property Info', {
        'fields': ('property_utility',('bedroom', 'bathroom'), ('carpet_units', 'carpet_area'), ('builtup_units', 'builtup_area'), ('floor', 'total_floor'), 'vastu_exit', 'interiors', 'kitchen'),
        "classes": ('',)
    }),
    ('Location Info', {
        'fields': ('flat_number', 'wing', 'building_name', 'street_name','location', 'landmark', 'google_location', 'city', 'state', 'country'),
        'classes': ('',)
    }),
    ('Budget Info', {
        'fields': (('sale_price', 'ownership'), 'possession', 'possession_age', 'possession_due_date', 'parking', 'certifications'),
        'classes': ('',)
    }),
    ('Features Info', {
        'fields': ('amenities', 'other_features'),
        'classes': ('',)
    }),
    ('Inventory Info', {
        'fields': ( 'video_link', 'description'),
        'classes': ('',)
    }),
    ('Status Info', {
        'fields': ('property_status', 'delete_flag'),
        'classes': ('',)
    })
    )


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        obj.save()

    class Media:
        js = ('sale_inventory/js/possession_field.js',)

admin.site.register(SaleInventoryPenthouse, SaleInventoryPenthouseAdminClass)

#Commercial Office
class SaleInventoryCommercialOfficeAdminClass(admin.ModelAdmin):
    form = SaleInventoryCommercialOfficeForm
    actions = ['mark_as_delete_flag']
    list_filter = ('property_status', PropertyUtilityFilter,'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','cabin', 'work_stations','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','pantry','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','cabin', 'work_stations','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','pantry','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    
    fieldsets = (
    ('Contact Info', {
        'fields': ('contact_id', 'tags', 'notes'),
        'classes': ('',)
    }),
    ('Property Info', {
        'fields': ('property_utility',('cabin', 'work_stations', 'bathroom'), ('carpet_units', 'carpet_area'), ('builtup_units', 'builtup_area'), ('floor', 'total_floor'), 'vastu_exit', 'interiors', 'pantry'),
        "classes": ('',)
    }),
    ('Location Info', {
        'fields': ('office_no', 'wing', 'building_name', 'street_name','location', 'landmark', 'google_location', 'city', 'state', 'country'),
        'classes': ('',)
    }),
    ('Budget Info', {
        'fields': (('sale_price', 'ownership'), 'possession', 'possession_age', 'possession_due_date', 'parking', 'certifications'),
        'classes': ('',)
    }),
    ('Features Info', {
        'fields': ('amenities', 'other_features'),
        'classes': ('',)
    }),
    ('Inventory Info', {
        'fields': ( 'video_link', 'description'),
        'classes': ('',)
    }),
    ('Status Info', {
        'fields': ('property_status', 'delete_flag'),
        'classes': ('',)
    })
    )


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        obj.save()

    class Media:
        js = ('sale_inventory/js/possession_field.js',)

admin.site.register(SaleInventoryCommercialOffice, SaleInventoryCommercialOfficeAdminClass)

#Shop
class SaleInventoryShopAdminClass(admin.ModelAdmin):
    form = SaleInventoryShopForm
    actions = ['mark_as_delete_flag']
    list_filter = ('property_status', PropertyUtilityFilter,'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','partitions','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','partitions','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','floor','total_floor','vastu_exit','interiors','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    
    fieldsets = (
    ('Contact Info', {
        'fields': ('contact_id', 'tags', 'notes'),
        'classes': ('',)
    }),
    ('Property Info', {
        'fields': ('property_utility',('partitions', 'bathroom'), ('carpet_units', 'carpet_area'), ('builtup_units', 'builtup_area'), ('floor', 'total_floor'), 'vastu_exit', 'interiors'),
        "classes": ('',)
    }),
    ('Location Info', {
        'fields': ('shop_no', 'wing', 'building_name', 'street_name','location', 'landmark', 'google_location', 'city', 'state', 'country'),
        'classes': ('',)
    }),
    ('Budget Info', {
        'fields': (('sale_price', 'ownership'), 'possession', 'possession_age', 'possession_due_date', 'parking', 'certifications'),
        'classes': ('',)
    }),
    ('Features Info', {
        'fields': ('amenities', 'other_features'),
        'classes': ('',)
    }),
    ('Inventory Info', {
        'fields': ( 'video_link', 'description'),
        'classes': ('',)
    }),
    ('Status Info', {
        'fields': ('property_status', 'delete_flag'),
        'classes': ('',)
    })
    )


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        obj.save()

    class Media:
        js = ('sale_inventory/js/possession_field.js',)

admin.site.register(SaleInventoryShop, SaleInventoryShopAdminClass)

#Cottage
class SaleInventoryCottageAdminClass(admin.ModelAdmin):
    form = SaleInventoryCottageForm
    actions = ['mark_as_delete_flag']
    list_filter = ('property_status', PropertyUtilityFilter,'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','partitions','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','total_floor','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','partitions','bathroom','carpet_units','carpet_area','builtup_units','builtup_area','total_floor','vastu_exit','interiors','kitchen','location','city','state','country','sale_price','ownership','parking','certifications','amenities','other_features','property_status')
    
    fieldsets = (
    ('Contact Info', {
        'fields': ('contact_id', 'tags', 'notes'),
        'classes': ('',)
    }),
    ('Property Info', {
        'fields': ('property_utility',('partitions', 'bathroom'), ('carpet_units', 'carpet_area'), ('builtup_units', 'builtup_area'),'total_floor', 'vastu_exit', 'interiors','kitchen'),
        "classes": ('',)
    }),
    ('Location Info', {
        'fields': ('room_no', 'cts_no', 'society_name', 'street_name','location', 'landmark', 'google_location', 'city', 'state', 'country'),
        'classes': ('',)
    }),
    ('Budget Info', {
        'fields': (('sale_price', 'ownership'), 'possession', 'possession_age', 'possession_due_date', 'parking', 'certifications'),
        'classes': ('',)
    }),
    ('Features Info', {
        'fields': ('amenities', 'other_features'),
        'classes': ('',)
    }),
    ('Inventory Info', {
        'fields': ( 'video_link', 'description'),
        'classes': ('',)
    }),
    ('Status Info', {
        'fields': ('property_status', 'delete_flag'),
        'classes': ('',)
    })
    )


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        obj.save()

    class Media:
        js = ('sale_inventory/js/possession_field.js',)

admin.site.register(SaleInventoryCottage, SaleInventoryCottageAdminClass)