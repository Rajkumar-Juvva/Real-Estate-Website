from django import forms
from .models import *
from phonebook.models import Contacts
from choices import *
from django_select2.forms import Select2MultipleWidget
from django.core import validators


contact_id = forms.MultipleChoiceField(
    choices=((obj.id,obj.give_full_name()) for obj in Contacts.objects.all()),
    widget=Select2MultipleWidget(attrs={'class': 'form-control'}),
    required=False,
)
property_utility = forms.MultipleChoiceField(
    choices=PROPERTY_UTILITY_CHOICES,
    widget=Select2MultipleWidget(attrs={'class': 'form-control'}),
    required=True,
    error_messages={
        'required': 'select one or two options',
    },
    help_text='select one or two options',
    validators=[
        validators.MinLengthValidator(1, message='Select at least one option.'),
        validators.MaxLengthValidator(2, message='Select up to two options.')
    ]
)

class SaleInventoryFlatOrApartmentForm(forms.ModelForm):
    contact_id = contact_id
    property_utility =property_utility
    class Meta:
        model = flatOrApartment
        fields = '__all__'
        exclude = ["inventory_id"]

class SaleInventoryBungalowForm(forms.ModelForm):
    contact_id = contact_id
    property_utility =property_utility
    class Meta:
        model = SaleInventoryBungalow
        fields = '__all__'
        exclude = ["inventory_id"]
    
class SaleInventoryPenthouseForm(forms.ModelForm):
    contact_id = contact_id
    property_utility =property_utility
    class Meta:
        model = SaleInventoryPenthouse
        fields = '__all__'
        exclude = ["inventory_id"]

class SaleInventoryCommercialOfficeForm(forms.ModelForm):
    contact_id = contact_id
    property_utility =property_utility
    class Meta:
        model = SaleInventoryCommercialOffice
        fields = '__all__'
        exclude = ["inventory_id"]

class SaleInventoryShopForm(forms.ModelForm):
    contact_id = contact_id
    property_utility =property_utility
    class Meta:
        model = SaleInventoryShop
        fields = '__all__'
        exclude = ["inventory_id"]

class SaleInventoryCottageForm(forms.ModelForm):
    contact_id = contact_id
    property_utility =property_utility
    class Meta:
        model = SaleInventoryCottage
        fields = '__all__'
        exclude = ["inventory_id"]
    