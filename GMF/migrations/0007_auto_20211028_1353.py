# Generated by Django 3.2 on 2021-10-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMF', '0006_products_type_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='category',
            new_name='category_product',
        ),
        migrations.AddField(
            model_name='products',
            name='demanding',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='original',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]
