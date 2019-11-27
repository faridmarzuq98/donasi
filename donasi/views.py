from django.shortcuts import render
from django.template import Template, Context
from django.shortcuts import render_to_response

from django.views import generic
from .models import *

# Create your views here.
def index(request):
    return render_to_response('usr/index.html')

def about(request):
    return render_to_response('usr/about.html')

def campaign(request):
    return render_to_response('usr/campaign.html')

# @login_required
def campaign(request, template_name='usr/campaign.html'):
    terbaru = Campaign.objects.order_by('-pub_date')[:4]
    sedikit_lagi = Campaign.objects.order_by('-raised')[:3]
    data = {}
    data['campaign_terbaru'] = terbaru
    data['campaign_sedikit_lagi'] = sedikit_lagi
    return render(request, template_name, data)

def contact(request):
    return render_to_response('usr/contact.html')

def elements(request):
    return render_to_response('usr/elements.html')

def campaign_list(request):
    return render_to_response('usr/campaign_list.html')

def portfolio(request):
    return render_to_response('usr/portfolio.html')

def single_causes(request):
    return render_to_response('usr/single-causes.html')

def profile(request):
    return render_to_response('usr/profile.html')

#Admin side
def adm(request):
    return render_to_response('adm/index.html')

def error(request):
    return render_to_response('adm/error-404.html')

def material(request):
    return render_to_response('adm/icon-material.html')

#def profile(request):
#    return render_to_response('adm/pages-profile.html')

def starter(request):
    return render_to_response('adm/starter-kit.html')

def table(request):
    return render_to_response('adm/table-basic.html')
