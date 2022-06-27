from email.mime import image
from operator import mod
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
    nom_reduc = models.IntegerField()
    valeur_reduc = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return str(self.nom_reduction)

class Etat(models.Model):
    nom_etat = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.nom_etat

class Article(models.Model):

    CFA = 'XOF'
    EURO = '€'
    DOLLAR = '$'
    
    CURRENT_TYPE = [
        (CFA,'Xof'),
        (EURO,'euro'),
        (DOLLAR,'dollar')
    ]
    
    image = models.FileField()
    description = models.TextField()
    prix = models.IntegerField()
    promotion = models.BooleanField(default=False)
    valeur_reduction = models.IntegerField()
    nouveau = models.ForeignKey(Etat, on_delete=models.CASCADE)
    currencies = models.CharField(choices=CURRENT_TYPE,  max_length=255)
    reduction = models.BooleanField(default=False)
    collections = models.CharField(max_length=100, default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.image

 
