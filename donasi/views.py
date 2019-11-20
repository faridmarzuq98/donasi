from django.shortcuts import render
from django.template import Template, Context
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')
