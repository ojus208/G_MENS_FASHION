# Generated by Django 3.2 on 2021-10-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
