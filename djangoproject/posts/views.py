from django.shortcuts import render, redirect
from .forms import ResellerForm
from .models import Resellers


def home(request):
    resellers = Resellers.objects.all().order_by('first_name')

    context = {
        "title": "Latest Posts",
        "resellers": resellers
    }

    return render(request, "posts/index.html", context)


def add_reseller(request):
    form = ResellerForm(request.POST or None)

    context = {
        "title": "Latest Posts",
        "form": form,
        "field_names": {'first_name', 'last_name', 'email', 'phone'},
        "field_location": {'city', 'state', 'zipcode'}
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "posts/add-reseller.html", context)
