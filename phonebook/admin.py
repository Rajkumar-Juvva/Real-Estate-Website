from django.contrib import admin
from .models import Contacts, Emails, Phones
from django.contrib.auth.models import User
from .forms import PhonebookContactsForm
from django.contrib.auth.models import User

from django.forms import inlineformset_factory
from django.contrib.contenttypes.admin import GenericTabularInline



class EmailsInline(admin.TabularInline):
    model = Contacts.email.through
    extra = 1
    verbose_name_plural = 'Emails'
    # template = 'email_inline.html'
    

class PhonesInline(admin.TabularInline):
    model = Contacts.phone.through
    extra = 1
    verbose_name_plural = 'Phones'

class CreatedByFilter(admin.SimpleListFilter):
    title ="Created"
    parameter_name = "created_by"
    def lookups(self, request, model_admin):
        return [(obj.id,obj.get_full_name) for obj in User.objects.all()]
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(created_by = self.value())
        return queryset
    
class UpdatedByFilter(admin.SimpleListFilter):
    title = "Updated"
    parameter_name = "updated_by"
    def lookups(self, request, model_admin):
        return [(obj.id,obj.get_full_name) for obj in User.objects.all()]
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(updated_by = self.value())
        return queryset



@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id','prefix','first_name','middle_name','last_name','suffix','company_name','job_title','department','country','street_address','street_address_line_2','city','pincode','State','address_label','birthday','notes','created_at','updated_at','delete_flag')
    list_filter = ('contact_label',CreatedByFilter, 'created_at', UpdatedByFilter, 'updated_at', 'delete_flag')
    search_fields = ('id','prefix','first_name','middle_name','last_name','suffix','company_name','job_title','department','country','street_address','street_address_line_2','city','pincode','State','address_label','birthday','notes','created_at','updated_at','delete_flag')
    ordering = ('first_name', 'last_name')
    form = PhonebookContactsForm
    fieldsets = (
        ('Name', {
            'fields': ('prefix', 'first_name', 'middle_name', 'last_name', 'suffix')
        }),
        ("Contact", {
            'fields': (('email_address','email_label'),('phone_code','phone_number','phone_label'),'contact_label',),
        }),
        ('Details', {
            'fields': ('company_name', 'job_title', 'department','birthday')
        }),
        ('Address', {
            'fields': ('country', 'street_address', 'street_address_line_2', 'city', 'pincode', 'State', 'address_label')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ("Custom",{
            'fields':('facebook','twitter','linkedin','instagram','tiktok','youtube','custom_link')
        })

        )
    # inlines = [EmailsInline, PhonesInline]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user.id        
        obj.updated_by = request.user.id
        email = form.cleaned_data.get('email_address')
        email_label = form.cleaned_data.get('email_label')
        if email and email_label:
            if obj.email is None:
                email_obj, created = Emails.objects.get_or_create(email=email,email_label=email_label)
                obj.email.add = email_obj
            else:
                obj.email.update(email=email,email_label = email_label)

        phone_code = form.cleaned_data.get('phone_code')
        phone = form.cleaned_data.get('phone_number')
        phone_label = form.cleaned_data.get('phone_label')
        if phone_code and phone and phone_label:
            if obj.phone is None:
                phone_obj, created = Phones.objects.get_or_create(country_code=phone_code, phone=phone, phone_label=phone_label)
                obj.phone.add(phone_obj)
            else:
                obj.phone.update(phone = phone,phone_label = phone_label,country_code = phone_code)
        obj.save()
    class Media:
        # js = ('/static/js/email_phone_clone.js',)
        pass




# @admin.register(Emails)
# class EmailsAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Phones)
# class PhonesAdmin(admin.ModelAdmin):
#     pass