# Generated by Django 4.2.6 on 2023-11-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfits', '0003_outfit_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='imagen',
            field=models.ImageField(null=True, upload_to='outfit_images/'),
        ),
    ]