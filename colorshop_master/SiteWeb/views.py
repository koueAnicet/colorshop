from distutils.log import error
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
    reseaux = ReseauSocial.objects.all()
    return render(request,'colorshop_master/index.html', locals())

def contact(request):
    return render(request, 'colorshop_master/contact.html', locals())

def categorie(request):
    return render(request,'colorshop_master/categories.html', locals())

def categorie_get_id(request, categorie_id):
    
    try:
        categorie_ids = Categorie.objects.get(id=categorie_id)
        
        return render(request,'colorshop_master/categories.html', locals())
    except:
        data={
            "error": "pas trouver!"
        }
        return redirect("/", data)

        
def single(request):
    return render(request, 'colorshop_master/single.html', locals())

def single_get_id(request, single_id):
    try:
        #singles = Articles.objects.get(id=single_id)
       
        return render(request, 'colorshop_master/single.html', locals())
    except:
        data={
            'error': "Article introuvable",
        }
        return redirect('/', data)
def send_message(request):
    alert =""
    success = True
    error_message = "Message non envpoyé!"

    if request.method == "GET":
        return render(request, 'colorshop_master/contact.html', error_message)
    else:
        name_contact = request.POST['name']
        email_contact = request.POST['email']
        website_contact = request.POST['website']
        message_contact = request.POST['message']
        contacted = Contacted.objects.create(name_contact=name_contact, email_contact=email_contact, website_contact = website_contact, message_contact=message_contact)
        print(contacted)
        alert = 'envoyeé  reuissit!'
    
        data = {
        'alert': alert,
        'success': success
        }

        return redirect("contact",data)
 

def send_email(request):
    
    return redirect('/')
    
    