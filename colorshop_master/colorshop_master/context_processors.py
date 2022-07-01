from SiteWeb.models import*
from Shop.models import *

def global_Site_info(request):

   # site = Site.objects.first()
    return {
    #    "site_info": site,
    }   

def global_categorie(request):
    categorie = Categorie.objects.all()
    return {
        "categorie": categorie,
    }   

def global_article(request):
    single = Articles.objects.all()
    return {
        "categorie": single,
    }   
    
def global_reseau_social(request):
    reseaux = ReseauSocial.objects.all()
    return {
        "categorie": reseaux,
    }   