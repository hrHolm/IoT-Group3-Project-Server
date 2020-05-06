from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

from .forms import * 
from . import services
# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the dashboard index.")
    return render(request, "base_index.html")

def form_response(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SetpointForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            device_id = form.cleaned_data['device_id']
            setpoint_value = form.cleaned_data['setpoint_value']

            context = {
            'device_id': device_id,
            'setpoint_value': setpoint_value
            }
            services.pub_data_to_mqtt(topic="device/{id}/setpoint".format(id=device_id), message=json.dumps({'setpoint_value': setpoint_value}))
            #---------- redirect to a new URL:
            form = SetpointForm()
            return HttpResponseRedirect('/dashboard/success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SetpointForm()

    return render(request, 'setpoint.html', {'form': form})

def set_intensity(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IntensityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            device_id = form.cleaned_data['device_id']
            intensity_value = form.cleaned_data['intensity_value']

            context = {
            'device_id': device_id,
            'intensity_value': intensity_value
            }
            services.pub_data_to_mqtt(topic="device/{id}/intensity".format(id=device_id), message=json.dumps({'intensity_value': intensity_value}))
            #---------- redirect to a new URL:
            form = IntensityForm()
            return HttpResponseRedirect('/dashboard/success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IntensityForm()

    return render(request, 'intensity.html', {'form': form})

def success(request):
    return render(request, 'success.html')