# Generated by Django 4.0.5 on 2022-07-01 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_image1', models.FileField(blank=True, default=None, null=True, upload_to='cat_image1')),
                ('cat_image2', models.FileField(blank=True, default=None, null=True, upload_to='cat_image2')),
                ('cat_image3', models.FileField(blank=True, default=None, null=True, upload_to='cat_image3')),
                ('cat_image4', models.FileField(blank=True, default=None, null=True, upload_to='cat_image4')),
                ('cat_image5', models.FileField(blank=True, default=None, null=True, upload_to='cat_image5')),
                ('cat_image6', models.FileField(blank=True, default=None, null=True, upload_to='cat_image6')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='autre_image_article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='articles_images', to='Shop.categorieimages'),
            preserve_default=False,
        ),
    ]
