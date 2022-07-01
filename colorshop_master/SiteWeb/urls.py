from django.urls import path

from SiteWeb import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('contact/',views.contact, name = "contact"),
    path('all-categories/',views.categorie, name = "all_categories"),
    path('categories/<int:categorie_id>',views.categorie_get_id, name = "categories"),
    path('single/<int:single_id>',views.single_get_id, name = "Single"),
    path('single/',views.single, name = "single"),
   
]