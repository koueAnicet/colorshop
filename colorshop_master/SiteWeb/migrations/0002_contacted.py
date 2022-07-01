# Generated by Django 4.0.5 on 2022-07-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contact', models.CharField(max_length=50)),
                ('email_contact', models.EmailField(max_length=100)),
                ('website_contact', models.URLField(max_length=255)),
                ('message_contact', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
