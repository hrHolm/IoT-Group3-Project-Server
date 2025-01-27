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
            services.adjust_device(device_id=device_id, message=json.dumps({'setpoint_value': setpoint_value}))
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
            services.adjust_device(device_id=device_id, message=json.dumps({'intensity_value': intensity_value}))
            #---------- redirect to a new URL:
            form = IntensityForm()
            return HttpResponseRedirect('/dashboard/success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IntensityForm()

    return render(request, 'intensity.html', {'form': form})

def success(request):
    return render(request, 'success.html')


from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.subplots import make_subplots
from dashboard.models import DeviceData

def plot_values(request):
    x_data = []
    y1_data = []
    y2_data = []
    queryset = DeviceData.objects.all()
    for datum in queryset:
        x_data.append(datum.timestamp)
        y1_data.append(datum.light_value)
        y2_data.append(datum.setpoint_value)


    fig = make_subplots(shared_yaxes=True, shared_xaxes=True)

    fig.add_trace(Scatter(x=x_data, y=y1_data,
                        mode='markers', name='Monitored Light Level',
                        opacity=0.8, marker_color='green'))
    fig.add_trace(Scatter(x=x_data, y=y2_data,
                        mode='markers', name='Setpoint',
                        opacity=0.8, marker_color='red'))
    # Set x-axis title
    fig.update_xaxes(title_text="Timestamp [ns]")

    # Set y-axes titles
    fig.update_yaxes(title_text="Light Value [lx]")

    plot_div = plot(fig, output_type='div', include_plotlyjs=False, show_link=False, link_text="")
    return render(request, "base_plot.html", context={'plot_div': plot_div})
