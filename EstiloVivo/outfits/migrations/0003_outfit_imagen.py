# Generated by Django 4.2.6 on 2023-11-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfits', '0002_alter_outfit_color_prenda_alter_outfit_estilo_prenda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='outfit',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='outfit_images/'),
        ),
    ]
