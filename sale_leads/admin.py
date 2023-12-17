from django.contrib import admin
from .models import *
from .forms import *
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
    

class SaleLeadsFlatOrApartmentAdminClass(admin.ModelAdmin):
    form = SaleLeadFlatOrApartmentForm
    actions = ['mark_as_delete_flag']
    list_filter = ('lead_status',PropertyUtilityFilter, 'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','bedroom','bathroom','carpet_units','carpet_area_min','carper_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','bedroom','bathroom','carpet_units','carpet_area_min','carpet_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('contact_id', 'notes'),
            'classes': ('',)
        }),
        ('Lead Info', {
            'fields': ('property_utility',('bedroom', 'bathroom'), ('carpet_units', 'carpet_area_min','carpet_area_max',), ('builtup_units', 'builtup_area_min','builtup_area_max',), ('floor_min','floor_max',), 'vastu_exit', 'interiors', 'kitchen'),
            "classes": (''),
        }),
        ('Location Info', {
            'fields': ('location', 'google_location', 'city', 'state', 'country'),
            'classes': ('',)
        }),
        ('Budget Info', {
            'fields': (('budget_min', 'budget_max'),  'possession', 'possession_age', 'possession_due_date','ownership', 'parking', 'certifications'),
            'classes': ('',)
        }),
        ('Features Info', {
            'fields': ('amenities', 'other_features'),
            'classes': ('',)
        }),
        ('Description Info', {
            'fields': ( 'description',),
            'classes': ('',)
        }),
        ('Status Info', {
            'fields': ('lead_status', 'delete_flag'),
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
        js = ('sale_leads/js/possession_field.js',)

admin.site.register(flatOrApartment, SaleLeadsFlatOrApartmentAdminClass)

#Bungalow

class SaleLeadsBungalowAdminClass(admin.ModelAdmin):
    form = SaleLeadBungalowForm
    actions = ['mark_as_delete_flag']
    list_filter = ('lead_status',PropertyUtilityFilter, 'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','bedroom','bathroom','carpet_units','carpet_area_min','carper_area_max','builtup_units','builtup_area_min','builtup_area_max','total_floor','open_space','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','bedroom','bathroom','carpet_units','carpet_area_min','carpet_area_max','builtup_units','builtup_area_min','builtup_area_max','total_floor','open_space','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('contact_id', 'notes'),
            'classes': ('',)
        }),
        ('Lead Info', {
            'fields': ('property_utility',('bedroom', 'bathroom'), ('carpet_units', 'carpet_area_min','carpet_area_max',), ('builtup_units', 'builtup_area_min','builtup_area_max',),'total_floor','open_space', 'vastu_exit', 'interiors', 'kitchen'),
            "classes": (''),
        }),
        ('Location Info', {
            'fields': ('location', 'google_location', 'city', 'state', 'country'),
            'classes': ('',)
        }),
        ('Budget Info', {
            'fields': (('budget_min', 'budget_max'),'possession', 'possession_age', 'possession_due_date','ownership', 'parking', 'certifications'),
            'classes': ('',)
        }),
        ('Features Info', {
            'fields': ('amenities', 'other_features'),
            'classes': ('',)
        }),
        ('Description Info', {
            'fields': ( 'description',),
            'classes': ('',)
        }),
        ('Status Info', {
            'fields': ('lead_status', 'delete_flag'),
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
        js = ('sale_leads/js/possession_field.js',)

admin.site.register(SaleLeadsBungalow, SaleLeadsBungalowAdminClass)

#penthouse
class SaleLeadsPenthouseAdminClass(admin.ModelAdmin):
    form = SaleLeadPenthouseForm
    actions = ['mark_as_delete_flag']
    list_filter = ('lead_status',PropertyUtilityFilter, 'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','bedroom','bathroom','carpet_units','carpet_area_min','carper_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','bedroom','bathroom','carpet_units','carpet_area_min','carpet_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('contact_id', 'notes'),
            'classes': ('',)
        }),
        ('Lead Info', {
            'fields': ('property_utility',('bedroom', 'bathroom'), ('carpet_units', 'carpet_area_min','carpet_area_max',), ('builtup_units', 'builtup_area_min','builtup_area_max',), ('floor_min','floor_max',), 'vastu_exit', 'interiors', 'kitchen'),
            "classes": (''),
        }),
        ('Location Info', {
            'fields': ('location', 'google_location', 'city', 'state', 'country'),
            'classes': ('',)
        }),
        ('Budget Info', {
            'fields': (('budget_min', 'budget_max'),  'possession', 'possession_age', 'possession_due_date','ownership', 'parking', 'certifications'),
            'classes': ('',)
        }),
        ('Features Info', {
            'fields': ('amenities', 'other_features'),
            'classes': ('',)
        }),
        ('Description Info', {
            'fields': ( 'description',),
            'classes': ('',)
        }),
        ('Status Info', {
            'fields': ('lead_status', 'delete_flag'),
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
        js = ('sale_leads/js/possession_field.js',)

admin.site.register(SaleLeadsPenthouse, SaleLeadsPenthouseAdminClass)

#Commercial Office
class SaleLeadsCommercialOfficetAdminClass(admin.ModelAdmin):
    form = SaleLeadCommercialOfficeForm
    actions = ['mark_as_delete_flag']
    list_filter = ('lead_status',PropertyUtilityFilter, 'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','cabin','work_stations','bathroom','carpet_units','carpet_area_min','carper_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','pantry','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','cabin','work_stations','bathroom','carpet_units','carpet_area_min','carpet_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','pantry','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('contact_id', 'notes'),
            'classes': ('',)
        }),
        ('Lead Info', {
            'fields': ('property_utility',('cabin','work_stations', 'bathroom'), ('carpet_units', 'carpet_area_min','carpet_area_max',), ('builtup_units', 'builtup_area_min','builtup_area_max',), ('floor_min','floor_max',), 'vastu_exit', 'interiors', 'pantry'),
            "classes": (''),
        }),
        ('Location Info', {
            'fields': ('location', 'google_location', 'city', 'state', 'country'),
            'classes': ('',)
        }),
        ('Budget Info', {
            'fields': (('budget_min', 'budget_max'),  'possession', 'possession_age', 'possession_due_date','ownership', 'parking', 'certifications'),
            'classes': ('',)
        }),
        ('Features Info', {
            'fields': ('amenities', 'other_features'),
            'classes': ('',)
        }),
        ('Description Info', {
            'fields': ( 'description',),
            'classes': ('',)
        }),
        ('Status Info', {
            'fields': ('lead_status', 'delete_flag'),
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
        js = ('sale_leads/js/possession_field.js',)

admin.site.register(SaleLeadsCommercialOffice, SaleLeadsCommercialOfficetAdminClass)

#Shop
class SaleLeadsShopAdminClass(admin.ModelAdmin):
    form = SaleLeadShopForm
    actions = ['mark_as_delete_flag']
    list_filter = ('lead_status',PropertyUtilityFilter, 'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','partitions','bathroom','carpet_units','carpet_area_min','carper_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','partitions','bathroom','carpet_units','carpet_area_min','carpet_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('contact_id', 'notes'),
            'classes': ('',)
        }),
        ('Lead Info', {
            'fields': ('property_utility',('partitions', 'bathroom'), ('carpet_units', 'carpet_area_min','carpet_area_max',), ('builtup_units', 'builtup_area_min','builtup_area_max',), ('floor_min','floor_max',), 'vastu_exit', 'interiors'),
            "classes": (''),
        }),
        ('Location Info', {
            'fields': ('location', 'google_location', 'city', 'state', 'country'),
            'classes': ('',)
        }),
        ('Budget Info', {
            'fields': (('budget_min', 'budget_max'),  'possession', 'possession_age', 'possession_due_date','ownership', 'parking', 'certifications'),
            'classes': ('',)
        }),
        ('Features Info', {
            'fields': ('amenities', 'other_features'),
            'classes': ('',)
        }),
        ('Description Info', {
            'fields': ( 'description',),
            'classes': ('',)
        }),
        ('Status Info', {
            'fields': ('lead_status', 'delete_flag'),
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
        js = ('sale_leads/js/possession_field.js',)

admin.site.register(SaleLeadsShop, SaleLeadsShopAdminClass)

#Cottage
class SaleLeadsCottageAdminClass(admin.ModelAdmin):
    form = SaleLeadCottageForm
    actions = ['mark_as_delete_flag']
    list_filter = ('lead_status',PropertyUtilityFilter, 'delete_flag',)
    search_fields = ('inventory_id','contact_id','property_utility','description','partitions','bathroom','carpet_units','carpet_area_min','carper_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    list_display = ('inventory_id', 'selected_contacts','property_utility','description','partitions','bathroom','carpet_units','carpet_area_min','carpet_area_max','builtup_units','builtup_area_min','builtup_area_max','floor_min','floor_max','vastu_exit','interiors','kitchen','location','city','state','country','budget_min','budget_max','ownership','parking','certifications','amenities','other_features','lead_status')
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('contact_id', 'notes'),
            'classes': ('',)
        }),
        ('Lead Info', {
            'fields': ('property_utility',('partitions', 'bathroom'), ('carpet_units', 'carpet_area_min','carpet_area_max',), ('builtup_units', 'builtup_area_min','builtup_area_max',), ('floor_min','floor_max',), 'vastu_exit', 'interiors', 'kitchen'),
            "classes": (''),
        }),
        ('Location Info', {
            'fields': ('location', 'google_location', 'city', 'state', 'country'),
            'classes': ('',)
        }),
        ('Budget Info', {
            'fields': (('budget_min', 'budget_max'),  'possession', 'possession_age', 'possession_due_date','ownership', 'parking', 'certifications'),
            'classes': ('',)
        }),
        ('Features Info', {
            'fields': ('amenities', 'other_features'),
            'classes': ('',)
        }),
        ('Description Info', {
            'fields': ( 'description',),
            'classes': ('',)
        }),
        ('Status Info', {
            'fields': ('lead_status', 'delete_flag'),
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
        js = ('sale_leads/js/possession_field.js',)

admin.site.register(SaleLeadsCottage, SaleLeadsCottageAdminClass)