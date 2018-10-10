from django.shortcuts import render, redirect
from .forms import ResellerForm
# Create your views here.


def home(request):
    form = ResellerForm(request.POST or None)

    context = {
        "title": "Latest Posts",
        "form": form,
        "field_names": {'first_name', 'last_name', 'state', 'country'}
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "posts/index.html", context)
