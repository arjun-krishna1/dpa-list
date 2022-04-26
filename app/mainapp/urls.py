from django.urls import include, path


from .views import (
    index,
    join,
    list_vendors,
    add_stakeholder,
    add_vendor,
)

urlpatterns = [
    path('', index, name='index'),
    path('join/', join, name='join'),
    path('<int:org_id>/', list_vendors, name='list_vendors'),
    path('<int:org_id>/add_stakeholder/', add_stakeholder, name='add_stakeholder'),
    path('<int:org_id>/add_vendor/', add_vendor, name='add_vendor'),
]
