# Generated by Django 4.2 on 2023-07-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='banner',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
