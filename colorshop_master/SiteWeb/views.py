from django.shortcuts import render
from SiteWeb.models import *

# Create your views here.

# Create your views here.
def index(request):
    site = Site.objects.first()
    banners = Banner.objects.first()
    return render(request, 'colorshop_master/index.html', locals())

def contact(request):
    return render(request, 'colorshop_master/contact.html', locals())