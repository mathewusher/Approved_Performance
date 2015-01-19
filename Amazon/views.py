from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
#    return HttpResponse("Approved Performance Amazon <a href='/Amazon/about'>About</a>")
    context = RequestContext(request)
    context_dict = {'boldmessage': "This is a bold font from the context"}
    return render_to_response('Amazon/index.html', context_dict, context)

def about(request):
    return HttpResponse("Approved Performance Amazon About Page <a href='/Amazon/'>Index</a>")