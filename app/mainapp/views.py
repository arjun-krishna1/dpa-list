from django.shortcuts import redirect, render


from .models import (
    Organization,
    Vendor,
    Stakeholder
)

from .forms import (
    OrganizationForm,
    VendorForm,
    StakeholderForm,
)


def index(request):
    return render(request, 'index.html')

def join(request):

    form = OrganizationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'join.html', context)

def list_vendors(request, org_id: int):
    org = Organization.objects.get(id=org_id)
    vendors = Vendor.objects.filter(organization=org)

    context = {
        'vendors': vendors,
        'org': org,
    }
    return render(request, 'list_vendors.html', context)

def add_stakeholder(request, org_id: int):

    form = StakeholderForm(request.POST or None)
    org = Organization.objects.get(id=org_id)
    
    if form.is_valid() and org:
        stak = Stakeholder(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
            organization=org,
        )    
        
        stak.save()


        return redirect('index')
    
    context = {
        'form': form,
    }
    return render(request, 'add_stakeholder.html', context)

def add_vendor(request, org_id: int):

    form = VendorForm(request.POST or None)
    org = Organization.objects.get(id=org_id)

    if form.is_valid() and org:
        vend = Vendor(
            name=form.cleaned_data.get('name'),
            dpa_url=form.cleaned_data.get('dpa_url'),
            pending=True,
            organization=org,
        )    
        
        vend.save()

        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'add_vendor.html', context)

