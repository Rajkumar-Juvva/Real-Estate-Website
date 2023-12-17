from django import forms
from .models import *
from phonebook.models import Contacts
from choices import *
from django.core import validators


from django_select2.forms import Select2MultipleWidget

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
location = forms.MultipleChoiceField(
    choices=(),
    widget=Select2MultipleWidget(attrs={'class': 'form-control'}),
    required=False,
)

pantry = forms.MultipleChoiceField(
    choices=[(i, str(i)) for i in range(11)],
    widget=Select2MultipleWidget(attrs={'class': 'form-control'}),
    required=False,
)


class SaleLeadFlatOrApartmentForm(forms.ModelForm):
    contact_id =contact_id
    property_utility = property_utility
    location = location
    class Meta:
        model = flatOrApartment
        fields = '__all__'
        exclude = ["inventory_id","video_link","total_floor"]

class SaleLeadBungalowForm(forms.ModelForm):
    contact_id =contact_id
    property_utility = property_utility
    location = location
    class Meta:
        model = SaleLeadsBungalow
        fields = '__all__'
        exclude = ["inventory_id","video_link"]
    
    
class SaleLeadPenthouseForm(forms.ModelForm):
    contact_id =contact_id
    property_utility = property_utility
    location = location
    class Meta:
        model = SaleLeadsPenthouse
        fields = '__all__'
        exclude = ["inventory_id","video_link","total_floor"]

class SaleLeadCommercialOfficeForm(forms.ModelForm):
    contact_id =contact_id
    property_utility = property_utility
    location = location
    pantry = pantry
    class Meta:
        model = SaleLeadsCommercialOffice
        fields = '__all__'
        exclude = ["inventory_id","video_link"]
    
class SaleLeadShopForm(forms.ModelForm):
    contact_id =contact_id
    property_utility = property_utility
    location = location
    class Meta:
        model = SaleLeadsShop
        fields = '__all__'
        exclude = ["inventory_id","video_link"]

class SaleLeadCottageForm(forms.ModelForm):
    contact_id =contact_id
    property_utility = property_utility
    location = location
    class Meta:
        model = SaleLeadsCottage
        fields = '__all__'
        exclude = ["inventory_id","video_link"]