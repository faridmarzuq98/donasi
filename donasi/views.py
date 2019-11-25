from django.shortcuts import render
from django.template import Template, Context
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')

def campaign(request):
    return render_to_response('campaign.html')

def contact(request):
    return render_to_response('contact.html')

def elements(request):
    return render_to_response('elements.html')

def campaign_list(request):
    return render_to_response('campaign_list.html')

def portfolio(request):
    return render_to_response('portfolio.html')

def single_causes(request):
    return render_to_response('single-causes.html')