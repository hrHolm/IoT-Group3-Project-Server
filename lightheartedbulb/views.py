from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def home_index(request):
    #return HttpResponse("Hello, world. You're at the dashboard index.")
    return redirect('/dashboard/')