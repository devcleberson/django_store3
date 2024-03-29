# Generated by Django 4.2.4 on 2023-08-25 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category_name',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='category/images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
