
from turtle import ondrag
from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom_cat = models.CharField(max_length=20)
    image_cat = models.FileField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.nom_cat

class Reduction(models.Model):
    pourcentage_reduc = models.IntegerField(default=None, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return str(self.pourcentage_reduc)


class Couleur(models.Model):
    nom_couleur = models.CharField(max_length=20) 
    caractere_coluleur = models.CharField(max_length=10) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.nom_couleur





class Articles(models.Model):

    CFA = 'XOF'
    EURO = '€'
    DOLLAR = '$'
    
    
    CURRENT_TYPE = [
        (CFA,'Xof'),
        (EURO,'euro'),
        (DOLLAR,'dollar')
    ]
    
    NOUVEAU = 'New'
    ANCIEN = 'Sale'
    NUL = ''
    
    ETAT_ARTICLE =(
        (NUL,""),
        (NOUVEAU,"new"),
        (ANCIEN,'sale')
    )
    TRES_PETIT='S'
    PETIT='M'
    MOYEN='L'
    GRAND='XL'
    TRES_GRAND='XXL'
    TAILLE = [
        (TRES_PETIT,'tres_petit'),
        (PETIT,'petit'),
        (MOYEN,'moyen'),
        (GRAND,'grand'),
        (TRES_GRAND,'tres_grand'),
    ]  
    image = models.FileField()
    
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    promotion = models.BooleanField(default=False)
    reduction = models.BooleanField(default=False)
    valeur_reduction = models.ForeignKey(Reduction,on_delete=models.CASCADE,default=None, blank=True, null=True)
    
    etat = models.CharField(choices=ETAT_ARTICLE, max_length=255,default=None, blank=True, null=True)
    currencies = models.CharField(choices=CURRENT_TYPE,  max_length=255)
    couleur = models.ForeignKey(Couleur, on_delete=models.CASCADE, default=False)
    taille = models.CharField(choices=TAILLE, max_length=255,default=None, blank=True, null=True)  
    collections = models.CharField(max_length=100, default=None, blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="nom_cate")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

 
class AutresImagesArticles(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="nom_article")
    cat_image1 = models.FileField(default=None, blank=True, null=True,upload_to="cat_image1")
    cat_image2 = models.FileField(default=None, blank=True, null=True,upload_to="cat_image2")
    cat_image3 = models.FileField(default=None, blank=True, null=True,upload_to="cat_image3")
    cat_image4 = models.FileField(default=None, blank=True, null=True,upload_to="cat_image4")
    cat_image5 = models.FileField(default=None, blank=True, null=True,upload_to="cat_image5")
    cat_image6 = models.FileField(default=None, blank=True, null=True,upload_to="cat_image6")
    def __str__(self):
        return str(self.article)