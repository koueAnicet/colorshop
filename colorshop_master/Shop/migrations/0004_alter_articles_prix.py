# Generated by Django 4.0.5 on 2022-07-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_autresimagesarticles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
