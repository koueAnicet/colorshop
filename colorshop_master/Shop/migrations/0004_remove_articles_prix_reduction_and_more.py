# Generated by Django 4.0.5 on 2022-06-30 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_articles_valeur_reduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='prix_reduction',
        ),
        migrations.AlterField(
            model_name='articles',
            name='valeur_reduction',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.reduction'),
        ),
    ]
