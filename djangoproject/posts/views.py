from django.shortcuts import render, redirect
from django.http import JsonResponse
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
        "field_first_row": {'first_name', 'last_name'},
        "field_names": {'first_name', 'last_name', 'email', 'phone'},
        "field_location": {'city', 'state', 'zipcode'},
        "field_geocode": {'latitude', 'longitude'}
    }

    if request.method == "POST":
        if form.is_valid():
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            instance = form.save(commit=False)

            try:
                latitude, longitude = get_location(address, city, state, zipcode)

                instance.latitude = latitude
                instance.longitude = longitude

                instance.save()
            except Exception as e:
                print(e)

            return redirect("home")

    return render(request, "posts/add-reseller.html", context)


def update_reseller(request, id):
    reseller = Resellers.objects.get(id=id)

    form = ResellerForm(request.POST or None, instance=reseller)

    context = {
        "title": "Update Reseller",
        "form": form,
        "reseller": reseller,
        "field_names": {'first_name', 'last_name', 'email', 'phone'},
        "field_location": {'city', 'state', 'zipcode'},
        "field_geocode": {'latitude', 'longitude'}
    }

    if request.method == "POST":
        if form.is_valid():
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            instance = form.save(commit=False)

            try:
                latitude, longitude = get_location(address, city, state, zipcode)

                instance.latitude = latitude
                instance.longitude = longitude

                instance.save()
            except Exception as e:
                print(e)

            return redirect("home")

    return render(request, "posts/update-reseller.html", context)


def reseller_data(self):

    resellers = Resellers.objects.all().order_by('first_name')

    response_data = {
        "resellers": []
    }

    for reseller in resellers:
        reseller_data = {}

        reseller_data['first_name'] = reseller.first_name
        reseller_data['last_name'] = reseller.last_name
        reseller_data['phone'] = str(reseller.phone)
        reseller_data['email'] = reseller.email
        reseller_data['company'] = reseller.company
        reseller_data['address'] = reseller.address
        reseller_data['city'] = reseller.city
        reseller_data['state'] = reseller.state
        reseller_data['zipcode'] = reseller.zipcode
        reseller_data['comments'] = reseller.comments
        reseller_data['latitude'] = reseller.latitude
        reseller_data['longitude'] = reseller.longitude

        response_data["resellers"].append(reseller_data)

    return JsonResponse(response_data)
