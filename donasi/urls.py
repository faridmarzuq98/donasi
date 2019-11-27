"""donasi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from donasi.views import *

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name = 'home'), #root
    url(r'^about/$', about, name = 'about'),
    url(r'^campaign/$', campaign, name = 'campaign'),
    url(r'^contact/$', contact, name = 'contact'),
    url(r'^elements/$', elements, name = 'elements'),
    url(r'^campaign_list/$', campaign_list, name = 'campaign_list'),
    #url(r'^portfolio/', portfolio, name = 'portfolio'),
    url(r'^single-causes/$', single_causes, name = 'single-causes'),
    url(r'^profile/$', profile, name = 'profile'),

    #Admin side
<<<<<<< HEAD
    url(r'^adm/$', adm, name = 'adm'),
    url(r'^adm/error$', error, name = 'adm/error'),
    url(r'^adm/material$', material, name = 'adm/material'),
    url(r'^adm/profile$', profile, name = 'adm/profile'),
    url(r'^adm/starter$', starter, name = 'adm/starter'),
    url(r'^adm/table$', table, name = 'adm/table'),

=======
    url(r'^adm/', adm, name = 'adm'),
>>>>>>> 42d7677ae8322d9d82841e18003e7937f7236d57
]

urlpatterns += staticfiles_urlpatterns()
