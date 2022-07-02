from django.contrib import admin
from Shop.models import*
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('views_image','nom_cat','created_at','updated_at','is_deleted')
    def views_image(self, obj): 
        return mark_safe(f'<img src="{obj.image_cat.url}" style="height:100px; width:200px">')
    
admin.site.register(Reduction)
admin.site.register(Couleur)

admin.site.register(Articles)
admin.site.register(AutresImagesArticles)
