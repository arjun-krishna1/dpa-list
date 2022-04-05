from django.contrib import admin

from .models import (
    Organization,
    Vendor,
    Stakeholder,
)

admin.site.register(Organization)
admin.site.register(Vendor)
admin.site.register(Stakeholder)
