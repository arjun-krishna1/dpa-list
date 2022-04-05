from django.forms import ModelForm
from .models import (
    Organization,
    Vendor,
    Stakeholder,
)

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'password', 'support_email']

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'dpa_url']

class StakeholderForm(ModelForm):
    class Meta:
        model = Stakeholder
        fields = ['name', 'email']