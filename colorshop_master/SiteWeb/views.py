from django.shortcuts import redirect, render
from SiteWeb.models import *
from Shop.models import *
# Create your views here.

# Create your views here.
def index(request):
    site = Site.objects.first()
    categories = Categorie.objects.all().order_by(('nom_cat'))
    articles = Articles.objects.all()
    singles = Articles.objects.all()
    return render(request,'colorshop_master/index.html', locals())

def contact(request):

    return render(request, 'colorshop_master/contact.html', locals())

def categorie(request, categorie_id):
    
    try:
        categorie_ids = Categorie.objects.get(id=categorie_id)
        
        return render(request,'colorshop_master/categories.html', locals())
    except:
        data={
            "error": "pas trouver!"
        }
        return redirect("/", data)

def single(request, single_id):
    try:
        single_ids = Articles.objects.get(id=single_id)
       
        return render(request, 'colorshop_master/single.html', locals())
    except:
        data={
            'error': "Article introuvable",
        }
        return redirect('/', data)
    