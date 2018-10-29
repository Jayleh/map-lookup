from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import ResellerForm, UploadFileForm
from .models import Resellers
from .location import get_location


def home(request):
    resellers = Resellers.objects.all().order_by('first_name')

    context = {
        "title": "Reseller Map",
        "resellers": resellers
    }

    return render(request, "mapapp/index.html", context)


def add_reseller(request):
    reseller_form = ResellerForm()
    file_form = UploadFileForm()

    context = {
        "title": "Add Reseller",
        "reseller_form": reseller_form,
        "file_form": file_form,
        "field_first_row": {'first_name', 'last_name'},
        "field_names": {'first_name', 'last_name', 'email', 'phone'},
        "field_location": {'city', 'state', 'zipcode'},
        "field_geocode": {'latitude', 'longitude'}
    }

    return render(request, "mapapp/add-reseller.html", context)


def add_one_reseller(request):
    reseller_form = ResellerForm(request.POST)
    file_form = UploadFileForm()

    context = {
        "title": "Add Reseller",
        "reseller_form": reseller_form,
        "file_form": file_form,
        "field_first_row": {'first_name', 'last_name'},
        "field_names": {'first_name', 'last_name', 'email', 'phone'},
        "field_location": {'city', 'state', 'zipcode'},
        "field_geocode": {'latitude', 'longitude'}
    }

    if request.method == "POST":
        if reseller_form.is_valid():
            first_name = reseller_form.cleaned_data['first_name']
            last_name = reseller_form.cleaned_data['last_name']
            address = reseller_form.cleaned_data['address']
            city = reseller_form.cleaned_data['city']
            state = reseller_form.cleaned_data['state']
            zipcode = reseller_form.cleaned_data['zipcode']

            instance = reseller_form.save(commit=False)

            try:
                latitude, longitude = get_location(address, city, state, zipcode)

                instance.latitude = latitude
                instance.longitude = longitude

                instance.save()
            except Exception as e:
                print(e)
                raise

            messages.success(request, f"{first_name} {last_name} successfully added.")

        else:
            messages.error(request, f"Oops, something went wrong.")

    return render(request, "mapapp/add-reseller.html", context)


def import_resellers(request):
    reseller_form = ResellerForm()
    file_form = UploadFileForm(request.POST, request.FILES)

    context = {
        "title": "Add Reseller",
        "reseller_form": reseller_form,
        "file_form": file_form,
        "field_first_row": {'first_name', 'last_name'},
        "field_names": {'first_name', 'last_name', 'email', 'phone'},
        "field_location": {'city', 'state', 'zipcode'},
        "field_geocode": {'latitude', 'longitude'}
    }

    if request.method == "POST":
        if file_form.is_valid():
            file_form.save()
            messages.success(request, f"Resellers succesfully imported.")

    return render(request, "mapapp/add-reseller.html", context)


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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
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

            messages.success(request, f"{first_name} {last_name} successfully updated.")

            return redirect("home")

        else:
            messages.error(request, f"Oops, something went wrong.")

            return redirect("home")

    return render(request, "mapapp/update-reseller.html", context)


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
