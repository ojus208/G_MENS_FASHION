# Generated by Django 3.2 on 2022-02-11 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GMF', '0015_auto_20220211_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='orders',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GMF.transaction'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GMF.auth_user'),
        ),
        migrations.AddField(
            model_name='sizes_stock',
            name='product_name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
