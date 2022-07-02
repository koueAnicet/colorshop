from SiteWeb.models import*
from Shop.models import *

def global_Site_info(request):

    site = Site.objects.first()
    return {
       "site": site,
    }   

def global_categorie(request):
    categorie = Categorie.objects.all()
    return {
        "categorie": categorie,
    }   

def global_article_single(request):
    single = Articles.objects.all()
    return {
        "single": single,
    }   
    
def global_reseau_social(request):
    reseaux = ReseauSocial.objects.all()
    return {
        "reseaux": reseaux,
    }   
def global_article(request):
    articles = Articles.objects.all()
    return{
        "articles": articles,
    }