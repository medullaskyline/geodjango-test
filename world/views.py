from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from models import WorldBorder
from forms import PointForm, WorldBorderForm


def index(request):

    form = WorldBorderForm()
    single_mpoly = WorldBorder.objects.get(id=1).mpoly
    return render(request, 'index.html', {'mpoly': single_mpoly,
                                          'form': form})


def get_point(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PointForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PointForm()

    return render(request, 'point_form.html', {'form': form})