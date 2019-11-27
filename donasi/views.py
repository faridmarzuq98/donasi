from django.shortcuts import render
from django.template import Template, Context
from django.shortcuts import render_to_response, render
from django.views import generic
from .models import *

# Create your views here.
def index(request):
    return render(request, 'usr/index.html', {'nbar': 'home'})

def about(request):
    return render(request, 'usr/about.html', {'nbar': 'about'})

def campaign(request):
    return render(request, 'usr/campaign.html', {'nbar': 'campaign'})

# @login_required
def campaign(request, template_name='usr/campaign.html'):
    terbaru = Campaign.objects.order_by('-pub_date')[:4]
    sedikit_lagi = Campaign.objects.order_by('-raised')[:3]
    data = {}
    data['campaign_terbaru'] = terbaru
    data['campaign_sedikit_lagi'] = sedikit_lagi
    return render(request, template_name, data, {'nbar': 'campaign'})

def contact(request):
    return render(request, 'usr/contact.html', {'nbar': 'contact'})

def elements(request):
    return render(request, 'usr/elements.html')

def campaign_list(request, template_name='usr/campaign_list.html'):
    campaign = Campaign.objects.all()
    data = {}
    data['campaigns'] = campaign
    return render(request, template_name, data)

# def campaign_list(request):
#     return render(request, 'usr/campaign_list.html', {'nbar': 'campaign'})

def portfolio(request):
    return render(request, 'usr/portfolio.html')

def single_causes(request):
    return render(request, 'usr/single-causes.html', {'nbar': 'campaign'})

def profile(request):
    return render(request, 'usr/profile.html', {'nbar': 'profile'})

#Admin side
def adm(request):
    return render(request, 'adm/index.html')

def error(request):
    return render(request, 'adm/error-404.html')

def material(request):
    return render(request, 'adm/icon-material.html')

#def profile(request):
#    return render(request, 'adm/pages-profile.html')

def starter(request):
    return render(request, 'adm/starter-kit.html')

def table(request):
    return render(request, 'adm/table-basic.html')


