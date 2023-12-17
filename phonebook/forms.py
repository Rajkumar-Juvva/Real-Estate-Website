from django import forms
from .models import Contacts,Emails,Phones
from choices import *



class PhonebookContactsForm(forms.ModelForm):
    email_address = forms.EmailField(label="Email")
    email_label = forms.ChoiceField(label="Email Label",choices=labels)
    phone_code = forms.CharField(label="Phone Code",initial="+91",widget=forms.TextInput(attrs={'size': '5'}))
    phone_number = forms.CharField(label="Phone")
    phone_label = forms.ChoiceField(label="Phone Label",choices=labels)
    class Meta:
        model = Contacts
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            if instance.email.all():
                self.fields['email_address'].initial = instance.email.all()[0].email
                self.fields['email_label'].initial = instance.email.all()[0].email_label
            if instance.phone.all():
                self.fields['phone_code'].initial = instance.phone.all()[0].country_code
                self.fields['phone_number'].initial = instance.phone.all()[0].phone
                self.fields['phone_label'].initial = instance.phone.all()[0].phone_label
        # self.fields['email_address'].initial = "Hello"

