# Generated by Django 4.0.5 on 2022-06-30 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='valeur_reduction',
        ),
    ]
