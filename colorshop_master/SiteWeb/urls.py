from django.urls import path

from SiteWeb import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('contact/',views.contact, name = "contact"),
    path('categories/<int:categorie_id>',views.categorie, name = "categories"),
   
]