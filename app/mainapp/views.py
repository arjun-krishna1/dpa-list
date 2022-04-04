from django.shortcuts import redirect, render

from .models import Organization
from .forms import OrganizationForm


def index(request):
    return render(request, "index.html")

def join(request):

    form = OrganizationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        "form": form,
    }
    return render(request, "join.html", context)

