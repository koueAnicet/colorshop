from django.db import models

# Create your models here.
# Create your models here.
class ReseauSocial(models.Model):
    icon_reseau = models.CharField(max_length=50)
    nom_reseau = models.CharField(max_length=50)
    lien_reseau = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.nom_reseau

class Site(models.Model):
    nom_site = models.CharField(max_length=50)
    image_site = models.FileField()
    title_site = models.CharField(max_length=50)
    description_site = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    reseau_social_site = models.ForeignKey(ReseauSocial, on_delete=models.CASCADE, related_name="reseau_social")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False) 
    def __str__(self):
        return self.title_site



class Contacted(models.Model):
    nom_contact = models.CharField(max_length=50)
    email_contact = models.EmailField(max_length=100)
    website_contact = models.URLField(max_length=255)
    message_contact = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.nom_contact


class NewsLetter(models.Model):
    email_news= models.EmailField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.email_news