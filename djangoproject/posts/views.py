from django.shortcuts import render, redirect
from .forms import ResellerForm
from .models import Resellers
from .location import get_location


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
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            try:
                latitude, longitude = get_location(address, city, state, zipcode)

                form.cleaned_data["latitude"] = latitude
                form.cleaned_data["longitude"] = longitude

                form.save()
            except Exception as e:
                print(e)

            return redirect("home")

    return render(request, "posts/add-reseller.html", context)
