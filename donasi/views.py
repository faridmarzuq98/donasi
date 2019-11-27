from django.template import Template, Context
from django.shortcuts import render_to_response, render
from django.views import generic
from .models import *

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'usr/index.html', {'nbar': 'home'})

def about(request):
    return render(request, 'usr/about.html', {'nbar': 'about'})

# @login_required
def campaign(request, template_name='usr/campaign.html'):
    terbaru = Campaign.objects.order_by('-pub_date')[:4]
    sedikit_lagi = Campaign.objects.order_by('-raised')[:3]
    data = {}
    data['campaign_terbaru'] = terbaru
    data['campaign_sedikit_lagi'] = sedikit_lagi
    data['nbar'] = 'campaign'
    return render(request, template_name, data)

def contact(request):
    return render(request, 'usr/contact.html', {'nbar': 'contact'})

def elements(request):
    return render(request, 'usr/elements.html')

def campaign_list(request, template_name='usr/campaign_list.html'):
    campaign = Campaign.objects.all()
    data = {}
    data['campaigns'] = campaign
    return render(request, template_name, data)

def portfolio(request):
    return render(request, 'usr/portfolio.html')

def single_causes(request):
    return render(request, 'usr/single-causes.html')

def profile(request):
    user = User.objects.all()
    data = {'user': user}
    return render(request, 'usr/profile.html', data)

#Admin side
def adm(request):
    return render(request, 'adm/index.html')

def error(request):
    return render(request, 'adm/error-404.html')

def material(request):
    return render(request, 'adm/icon-material.html')

def starter(request):
    return render(request, 'adm/starter-kit.html')

def table(request):
    return render(request, 'adm/table-basic.html')

####################################################

def register(request):
    if request.method=='GET':
        return render(request, 'auth/register.html')
    else:
        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')

        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
        user.save()
        request.session['id'] = user.id
        return redirect('/')

def login(request):
    if request.method=='GET':
        return render(request, 'auth/login.html')
    else:
        if (User.objects.filter(email=request.POST['login_email']).exists()):
            user = User.objects.filter(email=request.POST['login_email'])[0]
            if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
                request.session['id'] = user.id
                return redirect('/')
        return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'auth/success.html', context)

def logout(request):
    request.session['id'] = ''
    return redirect('/login')
