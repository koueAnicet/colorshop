from SiteWeb.models import*
from Shop.models import *

def global_Site_info(request):

    site = Site.objects.first()
    return {
    #    "site_info": site,
    }   

def global_article(request):
    categorie = Categorie.objects.all()
    return {
        "categorie": categorie,
    }   